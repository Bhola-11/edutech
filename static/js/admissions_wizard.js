/**
 * Multi-Step Admissions Application Wizard Controller
 */
class AdmissionsWizard {
    constructor(wizardFormId) {
        this.form = document.getElementById(wizardFormId);
        this.currentStep = 1;
        this.totalSteps = 3;
    }

    init() {
        if (!this.form) return;
        this.updateView();
        
        const nextBtn = document.getElementById('wizard-next-btn');
        const prevBtn = document.getElementById('wizard-prev-btn');

        if (nextBtn) nextBtn.addEventListener('click', () => this.nextStep());
        if (prevBtn) prevBtn.addEventListener('click', () => this.prevStep());
    }

    nextStep() {
        if (this.validateStep(this.currentStep)) {
            if (this.currentStep < this.totalSteps) {
                this.currentStep++;
                this.updateView();
            } else {
                this.form.submit();
            }
        }
    }

    prevStep() {
        if (this.currentStep > 1) {
            this.currentStep--;
            this.updateView();
        }
    }

    validateStep(step) {
        const stepContainer = document.getElementById(`wizard-step-${step}`);
        if (!stepContainer) return true;
        const requiredInputs = stepContainer.querySelectorAll('[required]');
        let isValid = true;

        requiredInputs.forEach(input => {
            if (!input.value.trim()) {
                input.classList.add('is-invalid');
                isValid = false;
            } else {
                input.classList.remove('is-invalid');
            }
        });

        return isValid;
    }

    updateView() {
        for (let i = 1; i <= this.totalSteps; i++) {
            const stepEl = document.getElementById(`wizard-step-${i}`);
            const badgeEl = document.getElementById(`step-indicator-${i}`);
            if (stepEl) {
                stepEl.style.display = (i === this.currentStep) ? 'block' : 'none';
            }
            if (badgeEl) {
                if (i === this.currentStep) {
                    badgeEl.className = 'badge bg-primary rounded-pill p-2';
                } else if (i < this.currentStep) {
                    badgeEl.className = 'badge bg-success rounded-pill p-2';
                } else {
                    badgeEl.className = 'badge bg-secondary rounded-pill p-2';
                }
            }
        }

        const prevBtn = document.getElementById('wizard-prev-btn');
        const nextBtn = document.getElementById('wizard-next-btn');

        if (prevBtn) prevBtn.style.display = (this.currentStep === 1) ? 'none' : 'inline-block';
        if (nextBtn) nextBtn.textContent = (this.currentStep === this.totalSteps) ? 'Submit Final Application' : 'Continue to Next Step';
    }
}
window.AdmissionsWizard = AdmissionsWizard;
