from django.db import transaction
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from drf_spectacular.utils import extend_schema
from .serializers import MenuCategorySerializer, MenuItemSerializer, ProductSerializer
from .models import MenuCategory, MenuItem, Products


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

    def create(self, request, *args, **kwargs):
        menu_item_data = request.data
        product_ids = menu_item_data.get('products', [])

        with transaction.atomic():
            try:
                existing_products = Products.objects.select_for_update().filter(pk__in=product_ids)
                if existing_products.count() == len(product_ids):
                    for product in existing_products:
                        product.quantity -= 1
                        product.save()
                    return super().create(request, *args, **kwargs)
                else:
                    return Response({"error": "Some products do not exist."}, status=400)
            except Products.DoesNotExist:
                return Response({"error": "Some products do not exist."}, status=400)


@extend_schema(tags=["Products"])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
