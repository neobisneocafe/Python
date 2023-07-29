from rest_framework import serializers
from .models import Order, Menu, UserProfile, Notification, WorkSchedule


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


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = ('day', 'start_time', 'end_time', 'is_weekend')