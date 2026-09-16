from rest_framework import viewsets, permissions
from .models import Institution, Campus, Faculty, AcademicDepartment, Classroom
from .serializers import InstitutionSerializer, CampusSerializer, DepartmentSerializer, ClassroomSerializer
from apps.core.permissions import IsInstitutionAdminUser

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]

class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.select_related('institution')
    serializer_class = CampusSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = AcademicDepartment.objects.select_related('faculty', 'campus')
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.select_related('campus')
    serializer_class = ClassroomSerializer
    permission_classes = [permissions.IsAuthenticated]
