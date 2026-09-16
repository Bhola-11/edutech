/**
 * Dynamic Client-Side Table Sorting, Filtering and CSV Export
 */
class DataTableController {
    constructor(tableId, searchInputId) {
        this.table = document.getElementById(tableId);
        this.searchInput = document.getElementById(searchInputId);
        this.sortColumn = -1;
        this.sortAscending = true;
    }

    init() {
        if (!this.table) return;

        if (this.searchInput) {
            this.searchInput.addEventListener('input', () => this.filterTable());
        }

        const headers = this.table.querySelectorAll('thead th[data-sortable]');
        headers.forEach((th, idx) => {
            th.style.cursor = 'pointer';
            th.addEventListener('click', () => this.sortTable(idx));
        });
    }

    filterTable() {
        const query = this.searchInput.value.toLowerCase();
        const rows = this.table.querySelectorAll('tbody tr');

        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(query) ? '' : 'none';
        });
    }

    sortTable(colIndex) {
        const tbody = this.table.querySelector('tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));

        if (this.sortColumn === colIndex) {
            this.sortAscending = !this.sortAscending;
        } else {
            this.sortColumn = colIndex;
            this.sortAscending = true;
        }

        rows.sort((a, b) => {
            const valA = a.children[colIndex].textContent.trim();
            const valB = b.children[colIndex].textContent.trim();

            const numA = parseFloat(valA);
            const numB = parseFloat(valB);

            if (!isNaN(numA) && !isNaN(numB)) {
                return this.sortAscending ? numA - numB : numB - numA;
            }
            return this.sortAscending ? valA.localeCompare(valB) : valB.localeCompare(valA);
        });

        rows.forEach(r => tbody.appendChild(r));
    }
}
window.DataTableController = DataTableController;
