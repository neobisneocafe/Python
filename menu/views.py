from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema
from .serializers import MenuCategorySerializer,MenuItemSerializer,ProductSerializer,MenuItemImageSerializer
from .models import MenuCategory,MenuItem,Product,MenuItemImage


@extend_schema(tags=["Menu Category"])
class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Menu Items"])
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Products"])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=["Menu Item Images"])
class MenuItemImageViewSet(viewsets.ModelViewSet):
    queryset = MenuItemImage.objects.all()
    serializer_class = MenuItemImageSerializer
    permission_classes = [permissions.AllowAny]
