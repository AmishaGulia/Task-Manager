
// let allTasks = [];
// let currentFilter = 'All';

// // Run as soon as the page loads
// document.addEventListener('DOMContentLoaded', () => {
//     console.log("Task Manager Ready");
//     fetchTasks();
// });

// /**
//  * CORE LOGIC: API COMMUNICATION
//  */

// // 1. Fetch all tasks from the server
// async function fetchTasks() {
//     try {
//         const response = await fetch('/tasks');
//         const data = await response.json();
        
//         // Overwrite local array with fresh data from database
//         allTasks = data;
        
//         console.log("Tasks Synced:", allTasks);
//         renderTasks();
//         updateStats();
//     } catch (error) {
//         console.error("Critical Error: Could not sync tasks", error);
//     }
// }

// // 2. Add a new task (Forces 'Pending' on server)
// async function addTask() {
//     const titleInput = document.getElementById('title');
//     const descInput = document.getElementById('desc');

//     if (!titleInput.value.trim()) {
//         alert("Task title cannot be empty!");
//         return;
//     }

//     const newTaskData = {
//         title: titleInput.value.trim(),
//         description: descInput.value.trim()
//     };

//     try {
//         const response = await fetch('/tasks', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify(newTaskData)
//         });

//         if (response.ok) {
//             console.log("New task created successfully");
//             titleInput.value = ''; // Clear input
//             descInput.value = '';  // Clear description
            
//             // Re-fetch everything to ensure the UI matches the database exactly
//             await fetchTasks();
//         }
//     } catch (error) {
//         console.error("Error adding task:", error);
//     }
// }

// // 3. Mark task as Completed
// async function completeTask(id) {
//     try {
//         const response = await fetch(`/tasks/${id}`, { method: 'PUT' });
//         if (response.ok) {
//             console.log(`Task ${id} marked as Done`);
//             await fetchTasks(); // Sync with server
//         }
//     } catch (error) {
//         console.error("Error completing task:", error);
//     }
// }

// // 4. Delete a task
// async function deleteTask(id) {
//     if (!confirm("Delete this task?")) return;

//     try {
//         const response = await fetch(`/tasks/${id}`, { method: 'DELETE' });
//         if (response.ok) {
//             console.log(`Task ${id} deleted`);
//             await fetchTasks(); // Sync with server
//         }
//     } catch (error) {
//         console.error("Error deleting task:", error);
//     }
// }

// /**
//  * UI LOGIC: RENDERING & STATS
//  */

// // Update the Progress Bar and counters
// function updateStats() {
//     const total = allTasks.length;
//     const completed = allTasks.filter(t => t.status === 'Completed').length;
//     const percentage = total === 0 ? 0 : Math.round((completed / total) * 100);

//     // Update Progress Bar
//     const bar = document.querySelector('.progress-fill-logic');
//     if (bar) bar.style.width = percentage + "%";

//     // Update Counter Text
//     const countText = document.getElementById('task-count-text');
//     if (countText) {
//         countText.innerText = total === 0 
//             ? "No tasks yet!" 
//             : `Completed ${completed} of ${total} tasks (${percentage}%)`;
//     }
// }

// // Change the view (All / Pending / Completed)
// function setFilter(filterType) {
//     currentFilter = filterType;
//     console.log("Filter changed to:", filterType);

//     // Update button colors
//     document.querySelectorAll('.filter-tabs button, .filter-bar button').forEach(btn => {
//         btn.classList.remove('active');
//     });
    
//     const activeBtn = document.getElementById(`btn-${filterType}`);
//     if (activeBtn) activeBtn.classList.add('active');

//     renderTasks();
// }

// // Draw the tasks on the screen
// function renderTasks() {
//     const listContainer = document.getElementById('taskList');
    
//     const filtered = allTasks.filter(t => {
//         if (currentFilter === 'All') return true;
//         return t.status === currentFilter;
//     });

//     if (filtered.length === 0) {
//         listContainer.innerHTML = `<div style="text-align:center; padding:20px; color:#94a3b8;">Nothing here!</div>`;
//         return;
//     }

//     listContainer.innerHTML = filtered.map(t => `
//         <div class="task-card ${t.status}">
//             <div class="task-info">
//                 <strong>${t.title}</strong>
//                 <p>${t.description || ''}</p>
//             </div>
//             <div class="task-actions">
//                 ${t.status === 'Pending' 
//                     ? `<button class="btn-done" onclick="completeTask(${t.id})">Done</button>` 
//                     : '<span class="done-label">✅ Done</span>'}
//                 <button class="btn-del-icon" onclick="deleteTask(${t.id})">🗑️</button>
//             </div>
//         </div>
//     `).join('');
// }
let allTasks = [];
let currentFilter = 'All';

// Run fetchTasks as soon as the page loads
document.addEventListener('DOMContentLoaded', fetchTasks);

// 1. GET ALL TASKS
async function fetchTasks() {
    try {
        const res = await fetch('/tasks');
        allTasks = await res.json();
        renderTasks();
        updateStats();
    } catch (err) {
        console.error("Error fetching tasks:", err);
    }
}

// 2. CREATE NEW TASK
async function addTask() {
    const titleInput = document.getElementById('title');
    const descInput = document.getElementById('desc');
    const dateInput = document.getElementById('end_date');

    if (!titleInput.value.trim()) {
        alert("Please enter a task title!");
        return;
    }

    const payload = {
        title: titleInput.value,
        description: descInput.value,
        end_date: dateInput.value
    };

    const res = await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });

    if (res.ok) {
        // Clear inputs
        titleInput.value = '';
        descInput.value = '';
        dateInput.value = '';
        fetchTasks(); // Refresh list
    }
}

// 3. CREATE SUBTASK
async function addSubtask(taskId) {
    const subInput = document.getElementById(`sub-in-${taskId}`);
    if (!subInput.value.trim()) return;

    const res = await fetch(`/tasks/${taskId}/subtasks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: subInput.value })
    });

    if (res.ok) {
        fetchTasks();
    }
}

// 4. TOGGLE SUBTASK (Check/Uncheck)
async function toggleSubtask(subId) {
    const res = await fetch(`/subtasks/${subId}`, { method: 'PUT' });
    if (res.ok) {
        fetchTasks();
    }
}

// 5. COMPLETE OR DELETE MAIN TASK
async function updateStatus(id, method) {
    const res = await fetch(`/tasks/${id}`, { method: method });
    if (res.ok) {
        fetchTasks();
    }
}

// 6. UPDATE PROGRESS BAR & STATS
function updateStats() {
    const total = allTasks.length;
    const completed = allTasks.filter(t => t.status === 'Completed').length;
    const percentage = total === 0 ? 0 : (completed / total) * 100;

    // Update the blue bar width
    const bar = document.querySelector('.progress-fill-logic');
    if (bar) bar.style.width = percentage + "%";
    
    // Update the text
    const text = document.getElementById('task-count-text');
    if (text) text.innerText = `${completed} of ${total} tasks completed`;
}

// 7. FILTER LOGIC
function setFilter(f) {
    currentFilter = f;
    // Update button colors
    document.querySelectorAll('.filter-tabs button').forEach(btn => btn.classList.remove('active'));
    document.getElementById(`btn-${f}`).classList.add('active');
    renderTasks();
}

// 8. RENDER HTML TO SCREEN
function renderTasks() {
    const container = document.getElementById('taskList');
    const filtered = allTasks.filter(t => currentFilter === 'All' || t.status === currentFilter);

    if (filtered.length === 0) {
        container.innerHTML = `<p style="text-align:center; color:gray; margin-top:20px;">No tasks here!</p>`;
        return;
    }

    container.innerHTML = filtered.map(t => `
        <div class="task-card ${t.status}">
            <div style="flex: 1;">
                <div style="margin-bottom: 8px;">
                    <span style="font-size: 0.7rem; color: #94a3b8;">📅 ${t.created_at}</span>
                    ${t.end_date ? `<span class="deadline-badge">🏁 Due: ${t.end_date}</span>` : ''}
                </div>
                <h3 style="margin: 0; color: #1e293b;">${t.title}</h3>
                <p style="font-size: 0.85rem; color: #64748b; margin: 5px 0;">${t.description || 'No description'}</p>

                <div class="subtask-section">
                    ${t.subtasks.map(s => `
                        <div class="sub-item">
                            <input type="checkbox" ${s.is_done ? 'checked' : ''} onchange="toggleSubtask(${s.id})">
                            <span class="${s.is_done ? 'strikethrough' : ''}">${s.title}</span>
                        </div>
                    `).join('')}
                    <div style="display: flex; gap: 5px; margin-top: 8px;">
                        <input type="text" id="sub-in-${t.id}" placeholder="Add step..." 
                               style="padding: 5px; font-size: 0.8rem; margin: 0; border-radius: 6px;">
                        <button onclick="addSubtask(${t.id})" 
                                style="padding: 0 10px; border-radius: 6px; cursor: pointer; border: 1px solid #ddd;">+</button>
                    </div>
                </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 10px; justify-content: center;">
                ${t.status === 'Pending' 
                    ? `<button class="btn-done" onclick="updateStatus(${t.id}, 'PUT')">Done</button>` 
                    : '<span style="color: #22c55e; font-weight: bold; font-size: 0.8rem;">Completed ✅</span>'}
                <button onclick="updateStatus(${t.id}, 'DELETE')" 
                        style="background: none; border: none; cursor: pointer; font-size: 1.1rem;">🗑️</button>
            </div>
        </div>
    `).join('');
}