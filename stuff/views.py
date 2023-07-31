from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import Employee, WorkSchedule
from .serializers import EmployeeSerializer, WorkScheduleSerializer


@extend_schema(tags=["Employee"])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@extend_schema(tags=["WorkSchedule"])
class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
