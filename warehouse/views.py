from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from warehouse.models import Branches, Warehouse, Category
from warehouse.serializers import BranchesSerializer, WarehouseSerializer, CategorySerializer


@extend_schema(tags=["Branches"])
class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


@extend_schema(tags=["WareHouse"])
class WareHouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


@extend_schema(tags=["Category"])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
