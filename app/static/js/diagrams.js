/**
 * Diagram viewer — Phase 1 (static SVG) + Phase 2 (Excalidraw interactive)
 */
(function () {
    'use strict';

    // Track loaded Excalidraw viewers to avoid re-initialization
    var loadedViewers = {};

    // Toggle between static SVG and Excalidraw interactive view
    document.querySelectorAll('.diagram-toggle-btn[data-diagram-id]').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var diagramId = this.dataset.diagramId;
            var excalidrawUrl = this.dataset.excalidrawUrl;
            if (!diagramId || !excalidrawUrl) return;

            var svgWrapper = document.getElementById('svg-' + diagramId);
            var excalidrawWrapper = document.getElementById('excalidraw-' + diagramId);
            if (!svgWrapper || !excalidrawWrapper) return;

            if (svgWrapper.style.display !== 'none') {
                // Switch to interactive
                svgWrapper.style.display = 'none';
                excalidrawWrapper.style.display = 'block';
                this.innerHTML = '<i class="bi bi-image"></i> Static';
                this.title = 'Switch to static image view';
                loadExcalidrawViewer(diagramId, excalidrawUrl);
            } else {
                // Switch to static
                svgWrapper.style.display = 'block';
                excalidrawWrapper.style.display = 'none';
                this.innerHTML = '<i class="bi bi-arrows-fullscreen"></i> Interactive';
                this.title = 'Switch to interactive view (pan & zoom)';
            }
        });
    });

    /**
     * Lazily load the Excalidraw viewer for a diagram.
     * Uses dynamic ESM import from esm.sh CDN — only fetched on demand.
     */
    async function loadExcalidrawViewer(diagramId, dataUrl) {
        if (loadedViewers[diagramId]) return;
        loadedViewers[diagramId] = true;

        var container = document.getElementById('excalidraw-' + diagramId);
        if (!container) return;

        try {
            // Fetch diagram scene data
            var response = await fetch(dataUrl);
            if (!response.ok) throw new Error('Failed to load diagram data');
            var sceneData = await response.json();

            // Dynamically import React + Excalidraw from CDN
            var [React, ReactDOMClient, ExcalidrawModule] = await Promise.all([
                import('https://esm.sh/react@18.3.1'),
                import('https://esm.sh/react-dom@18.3.1/client'),
                import('https://esm.sh/@excalidraw/excalidraw@0.17.6?alias=react:react@18.3.1')
            ]);

            var Excalidraw = ExcalidrawModule.Excalidraw;
            var isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';

            // Clear spinner and mount viewer
            container.innerHTML = '';
            container.style.height = '400px';

            var root = ReactDOMClient.createRoot(container);
            root.render(
                React.createElement(Excalidraw, {
                    initialData: {
                        elements: sceneData.elements || [],
                        appState: Object.assign({}, sceneData.appState || {}, {
                            viewBackgroundColor: isDark ? '#1c2128' : '#ffffff'
                        })
                    },
                    viewModeEnabled: true,
                    zenModeEnabled: true,
                    theme: isDark ? 'dark' : 'light',
                    UIOptions: {
                        canvasActions: {
                            changeViewBackgroundColor: false,
                            clearCanvas: false,
                            export: false,
                            loadScene: false,
                            saveToActiveFile: false,
                            toggleTheme: false
                        }
                    }
                })
            );

            // Listen for theme changes to update Excalidraw
            window.addEventListener('themechange', function (e) {
                var newDark = e.detail.theme === 'dark';
                root.render(
                    React.createElement(Excalidraw, {
                        initialData: {
                            elements: sceneData.elements || [],
                            appState: Object.assign({}, sceneData.appState || {}, {
                                viewBackgroundColor: newDark ? '#1c2128' : '#ffffff'
                            })
                        },
                        viewModeEnabled: true,
                        zenModeEnabled: true,
                        theme: newDark ? 'dark' : 'light',
                        UIOptions: {
                            canvasActions: {
                                changeViewBackgroundColor: false,
                                clearCanvas: false,
                                export: false,
                                loadScene: false,
                                saveToActiveFile: false,
                                toggleTheme: false
                            }
                        }
                    })
                );
            });

        } catch (err) {
            console.error('Excalidraw load error:', err);
            container.innerHTML =
                '<div class="alert alert-warning m-3">' +
                '<i class="bi bi-exclamation-triangle"></i> ' +
                'Could not load interactive view. ' +
                '<a href="#" onclick="location.reload();return false;">Retry</a>' +
                '</div>';
            loadedViewers[diagramId] = false;
        }
    }

    // Expose for whiteboard module
    window._loadExcalidrawViewer = loadExcalidrawViewer;
})();
