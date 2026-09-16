from rest_framework import viewsets, permissions
from .models import StudentProfile, InstructorProfile, AcademicCredential
from .serializers import StudentProfileSerializer, InstructorProfileSerializer, AcademicCredentialSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.select_related('user', 'program', 'current_semester')
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.select_related('user')
    serializer_class = InstructorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class AcademicCredentialViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicCredentialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AcademicCredential.objects.filter(user=self.request.user)
