from rest_framework import viewsets
from warehouse.models import Branches, Warehouse, Category
from warehouse.serializers import BranchesSerializer, WarehouseSerializer, CategorySerializer


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


class WareHouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


