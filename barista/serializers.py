from rest_framework import serializers

from stuff.models import WorkSchedule
from .models import Order, Menu, UserProfile


class OrderSerializer(serializers.ModelSerializer):
    table = serializers.IntegerField(required=False)

    class Meta:
        model = Order
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = '__all__'
