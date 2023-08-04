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

    def validate(self, data):
        products_data = self.initial_data.get("products", [])
        for product_id in products_data:
            try:
                product = Products.objects.get(pk=product_id)
                if product.quantity == 0:
                    raise serializers.ValidationError(
                        f"Product '{product.name}' has a quantity of 0, which is not allowed for creating a MenuItem."
                    )
            except Products.DoesNotExist:
                raise serializers.ValidationError(f"Product with ID {product_id} does not exist.")
        return data
