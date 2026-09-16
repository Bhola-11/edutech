from rest_framework import serializers
from .models import User, UserSessionLog
from apps.core.constants import UserRoleChoices

class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.CharField(source='get_role_display', read_only=True)
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'full_name', 'role', 'role_display', 'institution',
            'campus', 'department', 'phone_number', 'profile_photo',
            'bio', 'is_verified', 'two_factor_enabled', 'date_joined'
        ]
        read_only_fields = ['id', 'date_joined', 'is_verified']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role', 'phone_number']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSessionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSessionLog
        fields = ['id', 'ip_address', 'device_info', 'created_at', 'logged_out_at', 'is_expired']
