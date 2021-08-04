from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','first_name', 'last_name', 'last_login', 'date_joined']