<template>
  <div class="app-shell">
    <aside class="sidebar" :class="{ collapsed: isCollapsed }">
      <div class="sidebar-header">
        <div class="sidebar-brand" v-show="!isCollapsed">
          <h1>{{ t('nav.companyName') }}</h1>
          <span class="subtitle">{{ t('nav.subtitle') }}</span>
        </div>
        <button
          class="sidebar-toggle"
          @click="toggleSidebar"
          :aria-label="isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'"
        >
          <svg :class="{ 'icon-flipped': isCollapsed }" width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M11 3L6 9L11 15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </div>
      <nav class="sidebar-nav">
        <router-link to="/" :class="{ active: $route.path === '/' }" :title="t('nav.overview')">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <rect x="2.5" y="2.5" width="5.5" height="5.5" rx="1" stroke="currentColor" stroke-width="1.5"/>
            <rect x="10" y="2.5" width="5.5" height="5.5" rx="1" stroke="currentColor" stroke-width="1.5"/>
            <rect x="2.5" y="10" width="5.5" height="5.5" rx="1" stroke="currentColor" stroke-width="1.5"/>
            <rect x="10" y="10" width="5.5" height="5.5" rx="1" stroke="currentColor" stroke-width="1.5"/>
          </svg>
          <span class="nav-label">{{ t('nav.overview') }}</span>
        </router-link>
        <router-link to="/inventory" :class="{ active: $route.path === '/inventory' }" :title="t('nav.inventory')">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M2.5 5.5L9 2.5L15.5 5.5V12.5L9 15.5L2.5 12.5V5.5Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
            <path d="M2.5 5.5L9 8.5M9 8.5L15.5 5.5M9 8.5V15.5" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
          </svg>
          <span class="nav-label">{{ t('nav.inventory') }}</span>
        </router-link>
        <router-link to="/orders" :class="{ active: $route.path === '/orders' }" :title="t('nav.orders')">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M5 2.5H13C13.5523 2.5 14 2.94772 14 3.5V15.5L9 13L4 15.5V3.5C4 2.94772 4.44772 2.5 5 2.5Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
            <path d="M6.5 6H11.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M6.5 8.5H11.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          <span class="nav-label">{{ t('nav.orders') }}</span>
        </router-link>
        <router-link to="/spending" :class="{ active: $route.path === '/spending' }" :title="t('nav.finance')">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M9 2.5V15.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M12 5.5C12 5.5 10.5 4.5 9 4.5C7.5 4.5 6 5.25 6 6.75C6 8.25 7.5 8.75 9 9C10.5 9.25 12 9.75 12 11.25C12 12.75 10.5 13.5 9 13.5C7.5 13.5 6 12.5 6 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          <span class="nav-label">{{ t('nav.finance') }}</span>
        </router-link>
        <router-link to="/demand" :class="{ active: $route.path === '/demand' }" :title="t('nav.demandForecast')">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M2.5 12.5L7 8L10 11L15.5 5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M11.5 5.5H15.5V9.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span class="nav-label">{{ t('nav.demandForecast') }}</span>
        </router-link>
        <router-link to="/restocking" :class="{ active: $route.path === '/restocking' }" :title="t('nav.restocking')">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M15.5 9C15.5 12.5899 12.5899 15.5 9 15.5C6.5 15.5 4.5 14 3.3 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M2.5 9C2.5 5.41015 5.41015 2.5 9 2.5C11.5 2.5 13.5 4 14.7 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M3.3 12H2V13.3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M14.7 6H16V4.7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span class="nav-label">{{ t('nav.restocking') }}</span>
        </router-link>
        <router-link to="/reports" :class="{ active: $route.path === '/reports' }" title="Reports">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M5 2.5H11L14 5.5V15.5H5V2.5Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
            <path d="M11 2.5V5.5H14" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
            <path d="M7 9H12M7 11.5H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          <span class="nav-label">Reports</span>
        </router-link>
      </nav>
      <div class="sidebar-footer">
        <LanguageSwitcher :collapsed="isCollapsed" />
        <ProfileMenu
          :collapsed="isCollapsed"
          @show-profile-details="showProfileDetails = true"
          @show-tasks="showTasks = true"
        />
      </div>
    </aside>
    <div class="main-column">
      <div class="top-bar">
        <FilterBar />
      </div>
      <main class="main-content">
        <router-view />
      </main>
    </div>
  </div>

  <ProfileDetailsModal
    :is-open="showProfileDetails"
    @close="showProfileDetails = false"
  />

  <TasksModal
    :is-open="showTasks"
    :tasks="tasks"
    @close="showTasks = false"
    @add-task="addTask"
    @delete-task="deleteTask"
    @toggle-task="toggleTask"
  />
</template>

<script>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { api } from './api'
import { useAuth } from './composables/useAuth'
import { useI18n } from './composables/useI18n'
import FilterBar from './components/FilterBar.vue'
import ProfileMenu from './components/ProfileMenu.vue'
import ProfileDetailsModal from './components/ProfileDetailsModal.vue'
import TasksModal from './components/TasksModal.vue'
import LanguageSwitcher from './components/LanguageSwitcher.vue'

export default {
  name: 'App',
  components: {
    FilterBar,
    ProfileMenu,
    ProfileDetailsModal,
    TasksModal,
    LanguageSwitcher
  },
  setup() {
    const { currentUser } = useAuth()
    const { t } = useI18n()
    const showProfileDetails = ref(false)
    const showTasks = ref(false)
    const apiTasks = ref([])

    // Sidebar collapse: manual toggle + automatic default on smaller screens
    const isCollapsed = ref(false)
    const COLLAPSE_BREAKPOINT = 1024
    const checkScreenWidth = () => {
      isCollapsed.value = window.innerWidth < COLLAPSE_BREAKPOINT
    }
    const toggleSidebar = () => {
      isCollapsed.value = !isCollapsed.value
    }

    // Merge mock tasks from currentUser with API tasks
    const tasks = computed(() => {
      return [...currentUser.value.tasks, ...apiTasks.value]
    })

    const loadTasks = async () => {
      try {
        apiTasks.value = await api.getTasks()
      } catch (err) {
        console.error('Failed to load tasks:', err)
      }
    }

    const addTask = async (taskData) => {
      try {
        const newTask = await api.createTask(taskData)
        // Add new task to the beginning of the array
        apiTasks.value.unshift(newTask)
      } catch (err) {
        console.error('Failed to add task:', err)
      }
    }

    const deleteTask = async (taskId) => {
      try {
        // Check if it's a mock task (from currentUser)
        const isMockTask = currentUser.value.tasks.some(t => t.id === taskId)

        if (isMockTask) {
          // Remove from mock tasks
          const index = currentUser.value.tasks.findIndex(t => t.id === taskId)
          if (index !== -1) {
            currentUser.value.tasks.splice(index, 1)
          }
        } else {
          // Remove from API tasks
          await api.deleteTask(taskId)
          apiTasks.value = apiTasks.value.filter(t => t.id !== taskId)
        }
      } catch (err) {
        console.error('Failed to delete task:', err)
      }
    }

    const toggleTask = async (taskId) => {
      try {
        // Check if it's a mock task (from currentUser)
        const mockTask = currentUser.value.tasks.find(t => t.id === taskId)

        if (mockTask) {
          // Toggle mock task status
          mockTask.status = mockTask.status === 'pending' ? 'completed' : 'pending'
        } else {
          // Toggle API task
          const updatedTask = await api.toggleTask(taskId)
          const index = apiTasks.value.findIndex(t => t.id === taskId)
          if (index !== -1) {
            apiTasks.value[index] = updatedTask
          }
        }
      } catch (err) {
        console.error('Failed to toggle task:', err)
      }
    }

    onMounted(() => {
      loadTasks()
      checkScreenWidth()
      window.addEventListener('resize', checkScreenWidth)
    })

    onUnmounted(() => {
      window.removeEventListener('resize', checkScreenWidth)
    })

    return {
      t,
      showProfileDetails,
      showTasks,
      tasks,
      addTask,
      deleteTask,
      toggleTask,
      isCollapsed,
      toggleSidebar
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background: #f8fafc;
  color: #1e293b;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.app-shell {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 248px;
  flex-shrink: 0;
  height: 100vh;
  position: sticky;
  top: 0;
  background: #ffffff;
  border-right: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  transition: width 0.2s ease;
}

.sidebar-header {
  padding: 1.5rem 1.25rem;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.sidebar-brand {
  flex: 1;
  min-width: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.sidebar-toggle {
  flex-shrink: 0;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  color: #64748b;
  cursor: pointer;
  transition: all 0.2s ease;
}

.sidebar-toggle:hover {
  background: #f1f5f9;
  color: #0f172a;
}

.sidebar-toggle svg {
  transition: transform 0.2s ease;
}

.sidebar-toggle svg.icon-flipped {
  transform: rotate(180deg);
}

.sidebar-brand h1 {
  font-size: 1.375rem;
  font-weight: 700;
  color: #0f172a;
  letter-spacing: -0.025em;
}

.sidebar-brand .subtitle {
  font-size: 0.813rem;
  color: #64748b;
  font-weight: 400;
}

.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding: 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.sidebar-nav a {
  padding: 0.625rem 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  border-radius: 8px;
  color: #64748b;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.938rem;
  transition: all 0.2s ease;
}

.sidebar-nav a svg {
  flex-shrink: 0;
  width: 18px;
  height: 18px;
}

.sidebar-nav a:hover {
  color: #0f172a;
  background: #f1f5f9;
}

.sidebar-nav a.active {
  color: #2563eb;
  background: #eff6ff;
  font-weight: 600;
  /* negative margin offsets the added border width so content doesn't shift */
  margin-left: -3px;
  border-left: 3px solid #2563eb;
}

.sidebar.collapsed {
  width: 72px;
}

.sidebar.collapsed .sidebar-header {
  justify-content: center;
}

.sidebar.collapsed .sidebar-brand {
  display: none;
}

.sidebar.collapsed .nav-label {
  display: none;
}

.sidebar.collapsed .sidebar-nav a {
  justify-content: center;
  padding: 0.625rem;
  gap: 0;
}

.sidebar.collapsed .sidebar-nav a.active {
  margin-left: 0;
  border-left: none;
}

.sidebar-footer {
  margin-top: auto;
  padding: 0.875rem;
  border-top: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.main-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.top-bar {
  position: sticky;
  top: 0;
  z-index: 90;
  background: #ffffff;
  border-bottom: 1px solid #e2e8f0;
}

.main-content {
  flex: 1;
  width: 100%;
  padding: 1.5rem 2rem;
}

.page-header {
  margin-bottom: 1.5rem;
}

.page-header h2 {
  font-size: 1.875rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 0.375rem;
  letter-spacing: -0.025em;
}

.page-header p {
  color: #64748b;
  font-size: 0.938rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  background: white;
  padding: 1.25rem;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  transition: all 0.2s ease;
}

.stat-card:hover {
  border-color: #cbd5e1;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
}

.stat-label {
  color: #64748b;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.625rem;
}

.stat-value {
  font-size: 2.25rem;
  font-weight: 700;
  color: #0f172a;
  letter-spacing: -0.025em;
}

.stat-card.warning .stat-value {
  color: #ea580c;
}

.stat-card.success .stat-value {
  color: #059669;
}

.stat-card.danger .stat-value {
  color: #dc2626;
}

.stat-card.info .stat-value {
  color: #2563eb;
}

.card {
  background: white;
  border-radius: 10px;
  padding: 1.25rem;
  border: 1px solid #e2e8f0;
  margin-bottom: 1.25rem;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 0.875rem;
  border-bottom: 1px solid #e2e8f0;
}

.card-title {
  font-size: 1.125rem;
  font-weight: 700;
  color: #0f172a;
  letter-spacing: -0.025em;
}

.table-container {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
  border-bottom: 1px solid #e2e8f0;
}

th {
  text-align: left;
  padding: 0.5rem 0.75rem;
  font-weight: 600;
  color: #475569;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

td {
  padding: 0.5rem 0.75rem;
  border-top: 1px solid #f1f5f9;
  color: #334155;
  font-size: 0.875rem;
}

tbody tr {
  transition: background-color 0.15s ease;
}

tbody tr:hover {
  background: #f8fafc;
}

.badge {
  display: inline-block;
  padding: 0.313rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.025em;
}

.badge.success {
  background: #d1fae5;
  color: #065f46;
}

.badge.warning {
  background: #fed7aa;
  color: #92400e;
}

.badge.danger {
  background: #fecaca;
  color: #991b1b;
}

.badge.info {
  background: #dbeafe;
  color: #1e40af;
}

.badge.increasing {
  background: #d1fae5;
  color: #065f46;
}

.badge.decreasing {
  background: #fecaca;
  color: #991b1b;
}

.badge.stable {
  background: #e0e7ff;
  color: #3730a3;
}

.badge.high {
  background: #fecaca;
  color: #991b1b;
}

.badge.medium {
  background: #fed7aa;
  color: #92400e;
}

.badge.low {
  background: #dbeafe;
  color: #1e40af;
}

.loading {
  text-align: center;
  padding: 3rem;
  color: #64748b;
  font-size: 0.938rem;
}

.error {
  background: #fef2f2;
  border: 1px solid #fecaca;
  color: #991b1b;
  padding: 1rem;
  border-radius: 8px;
  margin: 1rem 0;
  font-size: 0.938rem;
}
</style>
