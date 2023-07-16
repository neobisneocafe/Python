from rest_framework import serializers
from .models import Branch, Employee,WorkSchedule

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = (
            'name',
            'position',
            'branch',
            'phone_number',
            'birth_date',
        )

class WorkScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSchedule
        fields = (
            'day_of_week',
            'start_time',
            'end_time',
            'employee'
        )
