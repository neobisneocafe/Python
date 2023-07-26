from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
from .serializers import MenuCategorySerializer,MenuItemSerializer,ProductSerializer,MenuItemImageSerializer
from .models import MenuCategory,MenuItem,Product,MenuItemImage


@extend_schema(tags=["Menu Category"])
class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@extend_schema(tags=["Menu Items"])
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Products"])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=["Menu Item Images"])
class MenuItemImageViewSet(viewsets.ModelViewSet):
    queryset = MenuItemImage.objects.all()
    serializer_class = MenuItemImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]