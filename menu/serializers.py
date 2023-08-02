from rest_framework import serializers
from .models import MenuCategory, MenuItem, Products


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = (
            'id',
            'name',
            'photo',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'id',
            'name',
            'weight',
            'arrival_date',
            'quantity',
            'min_limit',
        )


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = (
            'id',
            'name',
            'category',
            'products',
            'description',
            'price',
            'quantity',
            'min_limit',
            'arrivalDate',
            'image',
        )
