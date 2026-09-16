from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, UserSessionLog
from .serializers import UserSerializer, UserCreateSerializer, UserSessionLogSerializer
from apps.core.permissions import IsSuperAdminUser, IsInstitutionAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.select_related('institution', 'campus', 'department')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'create']:
            return [IsInstitutionAdminUser()]
        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class UserSessionLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSessionLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserSessionLog.objects.all()
        return UserSessionLog.objects.filter(user=self.request.user)
