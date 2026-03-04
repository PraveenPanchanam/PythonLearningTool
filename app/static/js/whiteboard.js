/**
 * Whiteboard — Full Excalidraw editor (Phase 3)
 * Loaded as an ES module via <script type="module">
 */

// --- State ---
let excalidrawAPI = null;
let currentDiagramId = null;
let lastSavedData = null;
let autoSaveTimer = null;
const config = window.WHITEBOARD_CONFIG || {};

// --- Import Excalidraw from CDN ---
async function initEditor() {
    const container = document.getElementById('whiteboard-container');
    const loading = document.getElementById('whiteboard-loading');
    if (!container) return;

    try {
        const [React, ReactDOMClient, ExcalidrawModule] = await Promise.all([
            import('https://esm.sh/react@18.3.1'),
            import('https://esm.sh/react-dom@18.3.1/client'),
            import('https://esm.sh/@excalidraw/excalidraw@0.17.6?alias=react:react@18.3.1')
        ]);

        const Excalidraw = ExcalidrawModule.Excalidraw;
        const isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';

        // Remove loading overlay
        if (loading) loading.remove();

        const root = ReactDOMClient.createRoot(container);

        function renderEditor(theme, initialData) {
            root.render(
                React.createElement(Excalidraw, {
                    initialData: initialData || {
                        elements: [],
                        appState: {
                            viewBackgroundColor: theme === 'dark' ? '#1c2128' : '#ffffff'
                        }
                    },
                    theme: theme,
                    excalidrawAPI: function (api) {
                        excalidrawAPI = api;
                    },
                    UIOptions: {
                        canvasActions: {
                            toggleTheme: false
                        }
                    },
                    onChange: function () {
                        // Debounced auto-save
                        clearTimeout(autoSaveTimer);
                        autoSaveTimer = setTimeout(autoSave, 30000);
                    }
                })
            );
        }

        renderEditor(isDark ? 'dark' : 'light');

        // Listen for theme changes
        window.addEventListener('themechange', function (e) {
            var newTheme = e.detail.theme;
            if (excalidrawAPI) {
                var elements = excalidrawAPI.getSceneElements();
                var appState = excalidrawAPI.getAppState();
                renderEditor(newTheme, {
                    elements: elements,
                    appState: Object.assign({}, appState, {
                        viewBackgroundColor: newTheme === 'dark' ? '#1c2128' : '#ffffff',
                        theme: newTheme
                    })
                });
            }
        });

    } catch (err) {
        console.error('Whiteboard init error:', err);
        if (loading) {
            loading.innerHTML =
                '<div class="alert alert-warning m-3">' +
                '<i class="bi bi-exclamation-triangle"></i> ' +
                'Could not load the editor. Please check your internet connection and ' +
                '<a href="#" onclick="location.reload();return false;">retry</a>.' +
                '</div>';
        }
    }
}

// --- Save / Load ---
function getSceneData() {
    if (!excalidrawAPI) return null;
    return {
        type: 'excalidraw',
        version: 2,
        elements: excalidrawAPI.getSceneElements(),
        appState: {
            viewBackgroundColor: excalidrawAPI.getAppState().viewBackgroundColor || '#ffffff',
            gridSize: null
        }
    };
}

async function saveDiagram() {
    var sceneData = getSceneData();
    if (!sceneData) return;

    var title = document.getElementById('diagram-title').value.trim() || 'Untitled Diagram';
    var statusEl = document.getElementById('save-status');

    if (statusEl) {
        statusEl.textContent = 'Saving...';
        statusEl.className = 'save-status saving';
    }

    try {
        var body = {
            title: title,
            data: sceneData,
            lesson_id: config.lessonId
        };
        if (currentDiagramId) {
            body.id = currentDiagramId;
        }

        var res = await fetch(config.saveUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': window.CSRF_TOKEN
            },
            body: JSON.stringify(body)
        });

        var result = await res.json();
        if (result.status === 'ok') {
            currentDiagramId = result.id;
            lastSavedData = JSON.stringify(sceneData);
            if (statusEl) {
                statusEl.textContent = 'Saved';
                statusEl.className = 'save-status saved';
                setTimeout(function () { statusEl.textContent = ''; }, 3000);
            }
            // Refresh sidebar
            refreshSidebar();
        }
    } catch (err) {
        console.error('Save error:', err);
        if (statusEl) {
            statusEl.textContent = 'Save failed';
            statusEl.className = 'save-status text-danger';
        }
    }
}

function autoSave() {
    if (!currentDiagramId) return; // Only auto-save if diagram has been saved before
    var sceneData = getSceneData();
    if (!sceneData) return;
    var currentData = JSON.stringify(sceneData);
    if (currentData !== lastSavedData) {
        saveDiagram();
    }
}

async function loadDiagram(diagramId) {
    try {
        var res = await fetch('/whiteboard/load/' + diagramId);
        var data = await res.json();
        if (data.error) return;

        currentDiagramId = data.id;
        document.getElementById('diagram-title').value = data.title;

        if (excalidrawAPI) {
            var isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
            excalidrawAPI.updateScene({
                elements: data.data.elements || [],
                appState: Object.assign({}, data.data.appState || {}, {
                    viewBackgroundColor: isDark ? '#1c2128' : '#ffffff'
                })
            });
            excalidrawAPI.scrollToContent();
        }

        lastSavedData = JSON.stringify(data.data);

        // Update active state in sidebar
        document.querySelectorAll('.load-diagram-btn').forEach(function (el) {
            el.classList.toggle('active', el.dataset.id == diagramId);
        });

    } catch (err) {
        console.error('Load error:', err);
    }
}

async function loadTemplate(url, title) {
    try {
        var res = await fetch(url);
        var data = await res.json();

        // Reset to new diagram
        currentDiagramId = null;
        document.getElementById('diagram-title').value = title + ' (copy)';

        if (excalidrawAPI) {
            var isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
            excalidrawAPI.updateScene({
                elements: data.elements || [],
                appState: Object.assign({}, data.appState || {}, {
                    viewBackgroundColor: isDark ? '#1c2128' : '#ffffff'
                })
            });
            excalidrawAPI.scrollToContent();
        }

        lastSavedData = null;
    } catch (err) {
        console.error('Template load error:', err);
    }
}

function newDiagram() {
    currentDiagramId = null;
    lastSavedData = null;
    document.getElementById('diagram-title').value = '';
    document.getElementById('save-status').textContent = '';

    if (excalidrawAPI) {
        var isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
        excalidrawAPI.updateScene({
            elements: [],
            appState: {
                viewBackgroundColor: isDark ? '#1c2128' : '#ffffff'
            }
        });
    }

    document.querySelectorAll('.load-diagram-btn').forEach(function (el) {
        el.classList.remove('active');
    });
}

async function refreshSidebar() {
    try {
        var res = await fetch(config.listUrl);
        var diagrams = await res.json();
        var list = document.getElementById('saved-list');
        if (!list) return;

        if (diagrams.length === 0) {
            list.innerHTML = '<p class="small text-muted mb-0">No saved diagrams yet.</p>';
            return;
        }

        list.innerHTML = diagrams.map(function (d) {
            var isActive = d.id === currentDiagramId ? ' active' : '';
            return '<a href="#" class="saved-item load-diagram-btn' + isActive + '" data-id="' + d.id + '">' +
                '<i class="bi bi-file-earmark-image"></i> ' + escapeHtml(d.title) +
                '<small class="text-muted d-block">' + timeAgo(d.updated_at) + '</small>' +
                '</a>';
        }).join('');

        // Re-bind events
        bindSidebarEvents();
    } catch (err) {
        console.error('Sidebar refresh error:', err);
    }
}

// --- Event Binding ---
function bindSidebarEvents() {
    document.querySelectorAll('.load-diagram-btn').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            loadDiagram(this.dataset.id);
        });
    });
}

// --- Utilities ---
function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

function timeAgo(isoStr) {
    var diff = (Date.now() - new Date(isoStr).getTime()) / 1000;
    if (diff < 60) return 'Just now';
    if (diff < 3600) return Math.floor(diff / 60) + 'm ago';
    if (diff < 86400) return Math.floor(diff / 3600) + 'h ago';
    if (diff < 604800) return Math.floor(diff / 86400) + 'd ago';
    return new Date(isoStr).toLocaleDateString();
}

// --- Init ---
document.addEventListener('DOMContentLoaded', function () {
    // Save button
    var saveBtn = document.getElementById('save-btn');
    if (saveBtn) saveBtn.addEventListener('click', saveDiagram);

    // New button
    var newBtn = document.getElementById('new-btn');
    if (newBtn) newBtn.addEventListener('click', newDiagram);

    // Load diagram buttons
    bindSidebarEvents();

    // Template buttons
    document.querySelectorAll('.load-template-btn').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            loadTemplate(this.dataset.url, this.dataset.title);
        });
    });

    // Initialize editor
    initEditor();
});
