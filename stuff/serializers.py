from rest_framework import serializers
from .models import Employee, WorkSchedule


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    workschedules = WorkScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'position',
            'branch',
            'phone_number',
            'birth_date',
            'workschedules',
        )
