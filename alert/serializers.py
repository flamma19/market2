from rest_framework import serializers
from alert.models import Alert
from django.conf import settings


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = (
            'title', 'symbol', 'author', 'id', 'high_price', 'low_price',
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name',)
        extra_kwargs = {'password': {'write_only': True}}