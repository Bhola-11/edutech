/**
 * Interactive Collegiate GPA Calculator & Forecaster
 */
class GPACalculator {
    constructor(tableBodyId, resultDisplayId) {
        this.tableBody = document.getElementById(tableBodyId);
        this.resultDisplay = document.getElementById(resultDisplayId);
        this.gradeScale = {
            'A+': 4.00, 'A': 4.00, 'A-': 3.70,
            'B+': 3.30, 'B': 3.00, 'B-': 2.70,
            'C+': 2.30, 'C': 2.00, 'C-': 1.70,
            'D+': 1.30, 'D': 1.00, 'F': 0.00
        };
    }

    addRow(courseName = '', credits = 3.0, defaultGrade = 'A') {
        if (!this.tableBody) return;
        const row = document.createElement('tr');
        row.className = 'gpa-calculator-row';
        row.innerHTML = `
            <td><input type="text" class="form-control form-control-sm course-name" value="${courseName}" placeholder="Course Title"></td>
            <td><input type="number" class="form-control form-control-sm course-credits" value="${credits}" step="0.5" min="1" max="6"></td>
            <td>
                <select class="form-select form-select-sm course-grade">
                    ${Object.keys(this.gradeScale).map(g => `<option value="${g}" ${g === defaultGrade ? 'selected' : ''}>${g} (${this.gradeScale[g].toFixed(2)})</option>`).join('')}
                </select>
            </td>
            <td class="text-center">
                <button type="button" class="btn btn-sm btn-outline-danger remove-row-btn">&times;</button>
            </td>
        `;
        row.querySelector('.remove-row-btn').addEventListener('click', () => {
            row.remove();
            this.calculate();
        });
        row.querySelector('.course-credits').addEventListener('input', () => this.calculate());
        row.querySelector('.course-grade').addEventListener('change', () => this.calculate());
        this.tableBody.appendChild(row);
        this.calculate();
    }

    calculate() {
        if (!this.tableBody) return;
        const rows = this.tableBody.querySelectorAll('.gpa-calculator-row');
        let totalCredits = 0;
        let totalPoints = 0;

        rows.forEach(row => {
            const credits = parseFloat(row.querySelector('.course-credits').value) || 0;
            const grade = row.querySelector('.course-grade').value;
            const pts = this.gradeScale[grade] !== undefined ? this.gradeScale[grade] : 0;
            totalCredits += credits;
            totalPoints += (credits * pts);
        });

        const gpa = totalCredits > 0 ? (totalPoints / totalCredits) : 0;
        if (this.resultDisplay) {
            this.resultDisplay.textContent = gpa.toFixed(2);
        }
    }
}
window.GPACalculator = GPACalculator;
