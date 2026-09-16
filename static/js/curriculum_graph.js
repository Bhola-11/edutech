/**
 * Curriculum Graph & Prerequisite Visualizer
 * Renders dynamic SVG nodes and directed dependency edges for academic course tracks.
 */
class CurriculumGraph {
    constructor(containerId, nodes = [], edges = []) {
        this.container = document.getElementById(containerId);
        this.nodes = nodes;
        this.edges = edges;
        this.svg = null;
        this.selectedNode = null;
    }

    init() {
        if (!this.container) return;
        this.render();
        window.addEventListener('resize', () => this.render());
    }

    render() {
        this.container.innerHTML = '';
        const width = this.container.clientWidth || 800;
        const height = Math.max(500, Math.ceil(this.nodes.length / 4) * 120);

        const svgNS = 'http://www.w3.org/2000/svg';
        this.svg = document.createElementNS(svgNS, 'svg');
        this.svg.setAttribute('width', width);
        this.svg.setAttribute('height', height);
        this.svg.style.backgroundColor = '#f8fafc';
        this.svg.style.borderRadius = '0.75rem';

        // Defs for arrow marker
        const defs = document.createElementNS(svgNS, 'defs');
        const marker = document.createElementNS(svgNS, 'marker');
        marker.setAttribute('id', 'arrowhead');
        marker.setAttribute('viewBox', '0 0 10 10');
        marker.setAttribute('refX', '8');
        marker.setAttribute('refY', '5');
        marker.setAttribute('markerWidth', '6');
        marker.setAttribute('markerHeight', '6');
        marker.setAttribute('orient', 'auto-start-reverse');

        const path = document.createElementNS(svgNS, 'path');
        path.setAttribute('d', 'M 0 0 L 10 5 L 0 10 z');
        path.setAttribute('fill', '#94a3b8');
        marker.appendChild(path);
        defs.appendChild(marker);
        this.svg.appendChild(defs);

        // Position nodes in academic term columns (Sem 1 to Sem 8)
        const colWidth = width / 5;
        const positions = {};

        this.nodes.forEach((node, idx) => {
            const col = (node.semester ? (node.semester - 1) % 4 : idx % 4) + 1;
            const row = Math.floor(idx / 4) + 1;
            positions[node.id] = {
                x: col * colWidth - (colWidth / 2),
                y: row * 110 - 40
            };
        });

        // Draw directed edges
        this.edges.forEach(edge => {
            const source = positions[edge.from];
            const target = positions[edge.to];
            if (source && target) {
                const line = document.createElementNS(svgNS, 'line');
                line.setAttribute('x1', source.x);
                line.setAttribute('y1', source.y);
                line.setAttribute('x2', target.x);
                line.setAttribute('y2', target.y);
                line.setAttribute('stroke', '#cbd5e1');
                line.setAttribute('stroke-width', '2');
                line.setAttribute('marker-end', 'url(#arrowhead)');
                this.svg.appendChild(line);
            }
        });

        // Draw nodes
        this.nodes.forEach(node => {
            const pos = positions[node.id];
            if (!pos) return;

            const g = document.createElementNS(svgNS, 'g');
            g.setAttribute('cursor', 'pointer');
            g.addEventListener('click', () => this.handleNodeClick(node));

            const rect = document.createElementNS(svgNS, 'rect');
            rect.setAttribute('x', pos.x - 70);
            rect.setAttribute('y', pos.y - 30);
            rect.setAttribute('width', 140);
            rect.setAttribute('height', 60);
            rect.setAttribute('rx', '8');
            rect.setAttribute('fill', node.completed ? '#dcfce7' : '#ffffff');
            rect.setAttribute('stroke', node.completed ? '#22c55e' : '#3b82f6');
            rect.setAttribute('stroke-width', '2');
            rect.setAttribute('filter', 'drop-shadow(0 2px 4px rgba(0,0,0,0.06))');

            const textCode = document.createElementNS(svgNS, 'text');
            textCode.setAttribute('x', pos.x);
            textCode.setAttribute('y', pos.y - 8);
            textCode.setAttribute('text-anchor', 'middle');
            textCode.setAttribute('font-weight', 'bold');
            textCode.setAttribute('font-size', '12');
            textCode.setAttribute('fill', '#1e293b');
            textCode.textContent = node.code;

            const textTitle = document.createElementNS(svgNS, 'text');
            textTitle.setAttribute('x', pos.x);
            textTitle.setAttribute('y', pos.y + 12);
            textTitle.setAttribute('text-anchor', 'middle');
            textTitle.setAttribute('font-size', '10');
            textTitle.setAttribute('fill', '#64748b');
            textTitle.textContent = (node.title.length > 20) ? node.title.substring(0, 18) + '...' : node.title;

            g.appendChild(rect);
            g.appendChild(textCode);
            g.appendChild(textTitle);
            this.svg.appendChild(g);
        });

        this.container.appendChild(this.svg);
    }

    handleNodeClick(node) {
        this.selectedNode = node;
        const detailsEl = document.getElementById('curriculum-node-details');
        if (detailsEl) {
            detailsEl.innerHTML = `
                <div class="card border-0 shadow-sm p-3">
                    <span class="badge bg-primary mb-2">${node.code}</span>
                    <h5 class="fw-bold mb-1">${node.title}</h5>
                    <p class="text-muted small mb-2">${node.credits} Credits &bull; Level: ${node.level || 'Undergraduate'}</p>
                    <p class="small text-secondary">${node.description || 'Core foundational curriculum requirement.'}</p>
                    <a href="/courses/${node.slug}/" class="btn btn-sm btn-primary">View Course Details</a>
                </div>
            `;
        }
    }
}
window.CurriculumGraph = CurriculumGraph;
