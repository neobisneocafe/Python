from rest_framework import serializers
from django import forms
from django.core.exceptions import ValidationError
from .models import Branch,Employee,WorkSchedule


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class WorkScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSchedule
        fields ='__all__'
        unique_together = ('employee', 'day_of_week')


    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get('employee')
        day_of_week = cleaned_data.get('day_of_week')

        if employee and day_of_week:
            # Проверяем, существует ли уже график работы для данного сотрудника и дня недели
            existing_schedules = WorkSchedule.objects.filter(employee=employee, day_of_week=day_of_week)
            if self.instance:
                existing_schedules = existing_schedules.exclude(pk=self.instance.pk)

            if existing_schedules.exists():
                raise forms.ValidationError("График работы для данного сотрудника и дня недели уже существует.")

        return cleaned_data

class EmployeeSerializer(serializers.ModelSerializer):
    branch= serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), allow_null=True)
    branch_info = serializers.SerializerMethodField()
    workschedules = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'position',
            'branch',
            'branch_info',
            'phone_number',
            'birth_date',
            'workschedules',
        )

    def get_branch_info(self, obj):
        if obj.branch:
            branch_data = BranchSerializer(obj.branch).data
            return branch_data
        return None

    def get_workschedules(self, obj):
        workschedule = WorkSchedule.objects.filter(employee=obj)
        workschedule_data = WorkScheduleSerializer(workschedule, many=True).data
        return workschedule_data