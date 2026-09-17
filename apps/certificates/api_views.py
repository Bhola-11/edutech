from rest_framework import viewsets, permissions
from .models import IssuedCertificate, DigitalBadge
from .serializers import IssuedCertificateSerializer, DigitalBadgeSerializer


class IssuedCertificateViewSet(viewsets.ModelViewSet):
    queryset = IssuedCertificate.objects.filter(is_revoked=False)
    serializer_class = IssuedCertificateSerializer
    permission_classes = [permissions.IsAuthenticated]


class DigitalBadgeViewSet(viewsets.ModelViewSet):
    queryset = DigitalBadge.objects.all()
    serializer_class = DigitalBadgeSerializer
    permission_classes = [permissions.IsAuthenticated]
