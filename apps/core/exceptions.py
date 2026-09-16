class EduTechException(Exception):
    def __init__(self, message=None, code=None, params=None):
        super().__init__(message)
        self.message = message or 'An unexpected error occurred in the enterprise education system.'
        self.code = code or 'generic_error'
        self.params = params or {}

class MultiTenantIsolationError(EduTechException):
    def __init__(self, message='Tenant isolation violation: Attempted cross-tenant access detected.'):
        super().__init__(message, code='tenant_isolation_violation')

class InactiveEntityError(EduTechException):
    def __init__(self, entity_name='Resource'):
        super().__init__(f'The requested {entity_name} is currently inactive or suspended.', code='inactive_resource')

class AcademicPrerequisiteNotMetError(EduTechException):
    def __init__(self, prerequisite_course):
        super().__init__(f'Enrollment prerequisite not met: Must complete {prerequisite_course}.', code='prerequisite_unmet')

class CapacityExceededError(EduTechException):
    def __init__(self, entity='Batch / Section'):
        super().__init__(f'Maximum allowable capacity exceeded for {entity}.', code='capacity_exceeded')

class DuplicateEnrollmentError(EduTechException):
    def __init__(self, message='Student is already actively enrolled in this course or batch.'):
        super().__init__(message, code='duplicate_enrollment')

class InvalidWorkflowStateTransitionError(EduTechException):
    def __init__(self, current_state, target_state):
        super().__init__(f'Illegal workflow state transition from {current_state} to {target_state}.', code='invalid_state_transition')
