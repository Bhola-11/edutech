from rest_framework import serializers
from .models import AdmissionCycle, AdmissionApplication, StudentEnrollment, Batch, CourseProgress

class AdmissionApplicationSerializer(serializers.ModelSerializer):
    applicant_name = serializers.CharField(source='applicant.get_full_name', read_only=True)

    class Meta:
        model = AdmissionApplication
        fields = '__all__'

class StudentEnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_code = serializers.CharField(source='course.code', read_only=True)

    class Meta:
        model = StudentEnrollment
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
