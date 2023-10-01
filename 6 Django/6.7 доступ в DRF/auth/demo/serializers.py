from rest_framework import serializers

from demo.models import Adv
from django.contrib.auth.models import User


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', 'created_at', 'open']
        read_only_fields = ['user',]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser', 'date_joined', 'is_staff']
        read_only_fields = ['is_superuser',]