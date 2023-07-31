from .models import Warehouse, Branches, WarehouseCategory
from rest_framework import serializers


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseCategory
        fields = '__all__'
