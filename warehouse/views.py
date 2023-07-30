from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from warehouse.models import Branches, Warehouse, WarehouseCategory
from warehouse.serializers import BranchesSerializer, WarehouseSerializer, WarehouseCategorySerializer


@extend_schema(tags=["Branches"])
class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


@extend_schema(tags=["WareHouse"])
class WareHouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


@extend_schema(tags=["WarehouseCategory"])
class WarehouseCategoryViewSet(viewsets.ModelViewSet):
    queryset = WarehouseCategory.objects.all()
    serializer_class = WarehouseCategorySerializer
