from drf_spectacular.utils import extend_schema
from rest_framework import viewsets


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
