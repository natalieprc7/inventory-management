"""
Tests for restocking API endpoints.
"""
import pytest


class TestRestockRecommendationsEndpoint:
    """Test suite for GET /api/restocking/recommendations."""

    def test_get_recommendations_with_budget(self, client):
        """Test getting recommendations with a generous budget."""
        response = client.get("/api/restocking/recommendations?budget=100000")
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

        first_item = data[0]
        required_fields = [
            "sku", "name", "category", "warehouse", "trend",
            "current_demand", "forecasted_demand", "unit_cost",
            "lead_time_days", "recommended_quantity", "estimated_cost"
        ]
        for field in required_fields:
            assert field in first_item, f"Missing field: {field}"

    def test_recommendations_sorted_by_demand_gap(self, client):
        """Test that recommendations prioritize the biggest forecast-vs-current gap first."""
        response = client.get("/api/restocking/recommendations?budget=100000")
        data = response.json()

        gaps = [item["forecasted_demand"] - item["current_demand"] for item in data]
        assert gaps == sorted(gaps, reverse=True)

    def test_recommendations_respect_budget(self, client):
        """Test that the total estimated cost never exceeds the given budget."""
        budget = 2000
        response = client.get(f"/api/restocking/recommendations?budget={budget}")
        assert response.status_code == 200

        data = response.json()
        total_cost = sum(item["estimated_cost"] for item in data)
        assert total_cost <= budget + 0.01

    def test_recommendations_exclude_decreasing_trend_item(self, client):
        """Test that items with a shrinking demand gap (e.g. MTR-304) are never recommended."""
        response = client.get("/api/restocking/recommendations?budget=100000")
        data = response.json()

        skus = [item["sku"] for item in data]
        assert "MTR-304" not in skus

    def test_recommendations_zero_budget_returns_empty(self, client):
        """Test that a zero budget yields no recommendations."""
        response = client.get("/api/restocking/recommendations?budget=0")
        assert response.status_code == 200

        data = response.json()
        assert data == []

    def test_recommendation_quantities_are_positive_ints(self, client):
        """Test that recommended quantities are always positive integers."""
        response = client.get("/api/restocking/recommendations?budget=5000")
        data = response.json()

        for item in data:
            assert isinstance(item["recommended_quantity"], int)
            assert item["recommended_quantity"] > 0


class TestSubmitRestockOrderEndpoint:
    """Test suite for POST /api/restocking/orders."""

    def test_submit_restock_order_creates_order(self, client):
        """Test that submitting a restock order returns a correctly-populated order."""
        payload = {
            "items": [
                {"sku": "WDG-001", "name": "Industrial Widget Type A", "quantity": 10, "unit_cost": 42.50}
            ]
        }
        response = client.post("/api/restocking/orders", json=payload)
        assert response.status_code == 200

        order = response.json()
        assert order["source"] == "restock"
        assert order["status"] == "Processing"
        assert order["customer"] == "Internal Restocking"
        assert abs(order["total_value"] - 425.0) < 0.01
        assert order["lead_time_days"] == 10

    def test_submit_restock_order_uses_max_lead_time_across_items(self, client):
        """Test that a multi-item order's lead time is gated by its slowest item."""
        payload = {
            "items": [
                {"sku": "WDG-001", "name": "Industrial Widget Type A", "quantity": 1, "unit_cost": 42.50},
                {"sku": "MTR-304", "name": "Electric Motor 5HP", "quantity": 1, "unit_cost": 410.00}
            ]
        }
        response = client.post("/api/restocking/orders", json=payload)
        assert response.status_code == 200

        order = response.json()
        assert order["lead_time_days"] == 14

    def test_submit_restock_order_appears_in_orders_list(self, client):
        """Test that a submitted restock order shows up in GET /api/orders."""
        payload = {
            "items": [
                {"sku": "GSK-203", "name": "High-Temperature Gasket", "quantity": 5, "unit_cost": 6.75}
            ]
        }
        create_response = client.post("/api/restocking/orders", json=payload)
        assert create_response.status_code == 200
        created_order = create_response.json()

        orders_response = client.get("/api/orders")
        all_orders = orders_response.json()

        matching = [o for o in all_orders if o["order_number"] == created_order["order_number"]]
        assert len(matching) == 1
        assert matching[0]["source"] == "restock"

    def test_submit_restock_order_empty_items_rejected(self, client):
        """Test that an empty item list is rejected with a 400."""
        response = client.post("/api/restocking/orders", json={"items": []})
        assert response.status_code == 400

        data = response.json()
        assert "detail" in data
