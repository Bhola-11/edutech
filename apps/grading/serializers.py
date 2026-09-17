from rest_framework import serializers
from .models import GradingScale, ScaleGradeLevel, GradeCategory, GradeItem, StudentGrade, FinalCourseGrade


class ScaleGradeLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScaleGradeLevel
        fields = '__all__'


class GradingScaleSerializer(serializers.ModelSerializer):
    levels = ScaleGradeLevelSerializer(many=True, read_only=True)

    class Meta:
        model = GradingScale
        fields = '__all__'


class FinalCourseGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalCourseGrade
        fields = '__all__'
