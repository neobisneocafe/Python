from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from .models import Order, MenuItem, UserProfile

from .serializers import OrderSerializer, MenuSerializer, UserProfileSerializer


@extend_schema(tags=["Order"])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()
        order_instance = serializer.instance

        for menu_item in order_instance.order_content.all():
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
