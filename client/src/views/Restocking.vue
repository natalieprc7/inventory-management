<template>
  <div class="restocking">
    <div class="page-header">
      <h2>{{ t('restocking.title') }}</h2>
      <p>{{ t('restocking.description') }}</p>
    </div>

    <div class="card budget-card">
      <div class="card-header">
        <h3 class="card-title">{{ t('restocking.budgetLabel') }}</h3>
        <span class="budget-value">{{ formatCurrency(budget) }}</span>
      </div>
      <input
        v-model.number="budget"
        type="range"
        min="0"
        max="50000"
        step="500"
        class="budget-slider"
      />
    </div>

    <div v-if="loading" class="loading">{{ t('common.loading') }}</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <div v-if="successMessage" class="success-banner">
        {{ successMessage }}
      </div>

      <div class="card">
        <div class="card-header">
          <h3 class="card-title">{{ t('restocking.recommendationsTitle') }}</h3>
        </div>

        <div v-if="recommendationRows.length === 0" class="empty-state">
          {{ t('restocking.noRecommendations') }}
        </div>
        <div v-else class="table-container">
          <table>
            <thead>
              <tr>
                <th>{{ t('restocking.table.include') }}</th>
                <th>{{ t('restocking.table.sku') }}</th>
                <th>{{ t('restocking.table.itemName') }}</th>
                <th>{{ t('restocking.table.category') }}</th>
                <th>{{ t('restocking.table.warehouse') }}</th>
                <th>{{ t('restocking.table.trend') }}</th>
                <th>{{ t('restocking.table.unitCost') }}</th>
                <th>{{ t('restocking.table.quantity') }}</th>
                <th>{{ t('restocking.table.lineCost') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="row in recommendationRows" :key="row.sku">
                <td>
                  <input type="checkbox" v-model="row.selected" />
                </td>
                <td><strong>{{ row.sku }}</strong></td>
                <td>{{ translateProductName(row.name) }}</td>
                <td>{{ row.category }}</td>
                <td>{{ translateWarehouse(row.warehouse) }}</td>
                <td>
                  <span :class="['badge', row.trend]">
                    {{ t(`trends.${row.trend}`) }}
                  </span>
                </td>
                <td>{{ formatCurrency(row.unit_cost) }}</td>
                <td>
                  <input
                    type="number"
                    min="0"
                    v-model.number="row.quantity"
                    class="quantity-input"
                  />
                </td>
                <td>{{ formatCurrency(lineCost(row)) }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div v-if="recommendationRows.length > 0" class="order-summary">
          <div class="summary-line" :class="{ 'over-budget': isOverBudget }">
            <span class="summary-label">{{ t('restocking.totalLabel') }}</span>
            <span class="summary-value">{{ formatCurrency(selectedTotal) }} / {{ formatCurrency(budget) }}</span>
          </div>
          <div v-if="isOverBudget" class="over-budget-warning">
            {{ t('restocking.overBudget') }}
          </div>

          <button
            class="place-order-btn"
            :disabled="!canPlaceOrder"
            @click="placeOrder"
          >
            {{ t('restocking.placeOrder') }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue'
import { api } from '../api'
import { useI18n } from '../composables/useI18n'
import { formatCurrency as formatCurrencyUtil } from '../utils/currency'

export default {
  name: 'Restocking',
  setup() {
    const { t, currentCurrency, translateProductName, translateWarehouse } = useI18n()

    const loading = ref(true)
    const error = ref(null)
    const budget = ref(10000)
    const recommendations = ref([])
    const recommendationRows = ref([])
    const successMessage = ref(null)

    const formatCurrency = (value) => {
      return formatCurrencyUtil(value, currentCurrency.value)
    }

    let debounceTimer = null

    const loadRecommendations = async () => {
      try {
        loading.value = true
        error.value = null
        recommendations.value = await api.getRestockRecommendations(budget.value)
      } catch (err) {
        error.value = 'Failed to load restock recommendations: ' + err.message
      } finally {
        loading.value = false
      }
    }

    watch(budget, () => {
      successMessage.value = null
      if (debounceTimer) clearTimeout(debounceTimer)
      debounceTimer = setTimeout(() => {
        loadRecommendations()
      }, 300)
    })

    watch(recommendations, (newRecommendations) => {
      recommendationRows.value = newRecommendations.map(item => ({
        ...item,
        selected: true,
        quantity: item.recommended_quantity
      }))
    })

    const lineCost = (row) => {
      return (row.quantity || 0) * row.unit_cost
    }

    const selectedTotal = computed(() => {
      return recommendationRows.value
        .filter(row => row.selected)
        .reduce((sum, row) => sum + lineCost(row), 0)
    })

    const isOverBudget = computed(() => selectedTotal.value > budget.value)

    const canPlaceOrder = computed(() => {
      const hasSelectedItems = recommendationRows.value.some(
        row => row.selected && row.quantity > 0
      )
      return hasSelectedItems && !isOverBudget.value
    })

    const placeOrder = async () => {
      try {
        error.value = null
        successMessage.value = null
        const items = recommendationRows.value
          .filter(row => row.selected && row.quantity > 0)
          .map(row => ({
            sku: row.sku,
            name: row.name,
            quantity: row.quantity,
            unit_cost: row.unit_cost
          }))

        const order = await api.submitRestockOrder(items)
        successMessage.value = t('restocking.orderSuccess', { orderNumber: order.order_number })
        await loadRecommendations()
      } catch (err) {
        error.value = t('restocking.orderError') + ': ' + err.message
      }
    }

    onMounted(loadRecommendations)

    return {
      t,
      loading,
      error,
      budget,
      recommendationRows,
      successMessage,
      formatCurrency,
      translateProductName,
      translateWarehouse,
      lineCost,
      selectedTotal,
      isOverBudget,
      canPlaceOrder,
      placeOrder
    }
  }
}
</script>

<style scoped>
.budget-card {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.budget-value {
  font-size: 1.25rem;
  font-weight: 700;
  color: #0f172a;
}

.budget-slider {
  width: 100%;
  accent-color: #2563eb;
}

.empty-state {
  text-align: center;
  padding: 2rem;
  color: #64748b;
  font-size: 0.938rem;
}

.quantity-input {
  width: 90px;
  padding: 0.375rem 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 0.875rem;
}

.order-summary {
  margin-top: 1.25rem;
  padding-top: 1.25rem;
  border-top: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.summary-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.summary-label {
  font-weight: 600;
  color: #475569;
}

.summary-value {
  font-size: 1.125rem;
  font-weight: 700;
  color: #0f172a;
}

.summary-line.over-budget .summary-value {
  color: #dc2626;
}

.over-budget-warning {
  color: #dc2626;
  font-size: 0.875rem;
  font-weight: 500;
}

.place-order-btn {
  align-self: flex-start;
  background: #2563eb;
  color: white;
  border: none;
  padding: 0.625rem 1.5rem;
  border-radius: 8px;
  font-size: 0.938rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease;
}

.place-order-btn:hover:not(:disabled) {
  background: #1d4ed8;
}

.place-order-btn:disabled {
  background: #cbd5e1;
  cursor: not-allowed;
}

.success-banner {
  background: #d1fae5;
  border: 1px solid #a7f3d0;
  color: #065f46;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1.25rem;
  font-size: 0.938rem;
}
</style>
