from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import Employee, Branch, WorkSchedule
from .serializers import EmployeeSerializer, BranchSerializer, WorkScheduleSerializer


@extend_schema(tags=["Employee"])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@extend_schema(tags=["Branch"])
class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


@extend_schema(tags=["WorkSchedule"])
class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer