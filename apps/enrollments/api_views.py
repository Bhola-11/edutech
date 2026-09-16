from rest_framework import viewsets, permissions
from .models import AdmissionApplication, StudentEnrollment, Batch
from .serializers import AdmissionApplicationSerializer, StudentEnrollmentSerializer, BatchSerializer

class AdmissionApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = AdmissionApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or getattr(self.request.user, 'is_institution_admin', False):
            return AdmissionApplication.objects.all()
        return AdmissionApplication.objects.filter(applicant=self.request.user)

class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or getattr(self.request.user, 'is_instructor', False):
            return StudentEnrollment.objects.all()
        return StudentEnrollment.objects.filter(student=self.request.user)

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.select_related('program', 'session')
    serializer_class = BatchSerializer
    permission_classes = [permissions.IsAuthenticated]
