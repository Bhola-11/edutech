from rest_framework import viewsets, permissions
from .models import Assessment, Question, AssessmentRubric
from .serializers import AssessmentSerializer, QuestionSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.filter(is_deleted=False)
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(is_deleted=False)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
