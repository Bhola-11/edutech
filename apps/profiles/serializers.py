from rest_framework import serializers
from .models import StudentProfile, InstructorProfile, AcademicCredential, SkillRecord

class StudentProfileSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = StudentProfile
        fields = '__all__'

class InstructorProfileSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = InstructorProfile
        fields = '__all__'

class AcademicCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicCredential
        fields = '__all__'
