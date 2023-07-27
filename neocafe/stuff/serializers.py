from rest_framework import serializers
from .models import Branch, Employee,WorkSchedule

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    branch= serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), allow_null=True)
    branch_info = serializers.SerializerMethodField()

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
        )
    def get_branch_info(self, obj):
        if obj.branch:
            branch_data = BranchSerializer(obj.branch).data
            return branch_data
        return None

class WorkScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSchedule
        fields ='__all__'
