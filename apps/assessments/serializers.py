from rest_framework import serializers
from .models import Assessment, Question, QuestionOption, AssessmentRubric, AssessmentSection


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ['id', 'option_text', 'option_html', 'is_correct', 'explanation', 'display_order']


class QuestionSerializer(serializers.ModelSerializer):
    options = QuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'course', 'category', 'title', 'question_type', 'prompt_html', 'explanation_html', 'default_points', 'negative_points', 'difficulty', 'blooms_level', 'options', 'is_active']


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['id', 'institution', 'course', 'title', 'slug', 'assessment_type', 'duration_minutes', 'total_points', 'passing_percentage', 'instructions_html', 'shuffle_questions', 'is_proctored', 'is_published', 'created_at']
