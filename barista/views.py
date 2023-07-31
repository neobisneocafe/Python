from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from stuff.models import WorkSchedule
from stuff.serializers import WorkScheduleSerializer
from .models import Order, MenuItem, UserProfile
from .serializers import (
    OrderSerializer,
    MenuSerializer,
    UserProfileSerializer,
)


@extend_schema(tags=["Order"])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['status']

    @action(detail=False, methods=['get'])
    def takeaway(self, request):
        orders = self.get_queryset().filter(status__in=['new', 'in_progress']).order_by('id')
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def in_institution(self, request):
        orders = self.get_queryset().filter(status__in=['ready']).order_by('id')
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)


@extend_schema(tags=["Menu"])
class MenuViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


@extend_schema(tags=["UserProfile"])
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
