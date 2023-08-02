from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
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

    def perform_create(self, serializer):
        serializer.save()
        order_instance = serializer.instance

        for product in order_instance.products.all():
            product.quantity -= 1
            product.save()

        for menu_item in order_instance.menu_items.all():
            menu_item.quantity -= 1
            menu_item.save()


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
