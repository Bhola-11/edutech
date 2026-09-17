from rest_framework import viewsets, permissions
from .models import ExamSession, ExamAttempt, ProctoringEvent
from .serializers import ExamSessionSerializer, ExamAttemptSerializer, ProctoringEventSerializer


class ExamSessionViewSet(viewsets.ModelViewSet):
    queryset = ExamSession.objects.all()
    serializer_class = ExamSessionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExamAttemptViewSet(viewsets.ModelViewSet):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProctoringEventViewSet(viewsets.ModelViewSet):
    queryset = ProctoringEvent.objects.all()
    serializer_class = ProctoringEventSerializer
    permission_classes = [permissions.IsAuthenticated]
