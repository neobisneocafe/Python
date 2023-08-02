from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import Employee, WorkSchedule, Branches
from .serializers import EmployeeSerializer, WorkScheduleSerializer, BranchesSerializer


@extend_schema(tags=["Branches"])
class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


@extend_schema(tags=["Employee"])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@extend_schema(tags=["WorkSchedule"])
class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
