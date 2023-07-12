from rest_framework import serializers
from .models import Branch, Employee

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = Employee
        fields = ['name', 'position', 'branch', 'phone_number', 'work_schedule']