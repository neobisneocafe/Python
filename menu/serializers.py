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


    def create(self, validated_data):
        if validated_data['quantity'] > validated_data['min_limit']:
            raise serializers.ValidationError(" Minimum limit cannot be less than the quantity.")

        return Products.objects.create(**validated_data)
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

    def create(self, validated_data):
        if validated_data['quantity'] > validated_data['min_limit']:
            raise serializers.ValidationError("Minimum limit cannot be less than the quantity.")

        return MenuItem.objects.create(**validated_data)

