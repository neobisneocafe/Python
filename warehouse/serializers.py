from .models import Warehouse,Category,Branches
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name','isdeleted']

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'