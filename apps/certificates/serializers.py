from rest_framework import serializers
from .models import CertificateTemplate, IssuedCertificate, DigitalBadge


class IssuedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedCertificate
        fields = '__all__'


class DigitalBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalBadge
        fields = '__all__'
