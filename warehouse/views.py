from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from warehouse.models import Branches, Ingredients, ReadyProducts
from warehouse.serializers import BranchesSerializer, IngredientsSerializer, ReadyProductsSerializer


@extend_schema(tags=["Branches"])
class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


@extend_schema(tags=["Ready_products"])
class ReadyProductsViewSet(viewsets.ModelViewSet):
    queryset = ReadyProducts.objects.all()
    serializer_class = ReadyProductsSerializer


@extend_schema(tags=["Ingredients"])
class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
