from rest_framework import viewsets, permissions
from .models import GradingScale, FinalCourseGrade
from .serializers import GradingScaleSerializer, FinalCourseGradeSerializer


class GradingScaleViewSet(viewsets.ModelViewSet):
    queryset = GradingScale.objects.all()
    serializer_class = GradingScaleSerializer
    permission_classes = [permissions.IsAuthenticated]


class FinalCourseGradeViewSet(viewsets.ModelViewSet):
    queryset = FinalCourseGrade.objects.all()
    serializer_class = FinalCourseGradeSerializer
    permission_classes = [permissions.IsAuthenticated]
