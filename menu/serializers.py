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
    def validate(self, data):
        min_limit = data.get("min_limit", 0)
        quantity = data.get("quantity", 0)

        if min_limit > quantity:
            raise serializers.ValidationError(
                {"detail": "Min limit can't be greater than quantity."}
            )

        return data

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



