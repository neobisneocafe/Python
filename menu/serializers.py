from rest_framework import serializers
from .models import MenuCategory, MenuItem, Product, MenuItemImage


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
        model = Product
        fields = (
            'id',
            'name',
            'weight',
            'arrival_date',
        )


class MenuItemSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(required=False),
        allow_empty=True,
        write_only=True,
        required=False,
    )

    class Meta:
        model = MenuItem
        fields = "__all__"
        extra_fields = (
            "url",
            "images",
        )

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        products_data = validated_data.pop("products", [])

        menu_item = MenuItem.objects.create(**validated_data)
        for product in products_data:
            menu_item.products.add(product)

        for image in uploaded_images:
            MenuItemImage.objects.create(image=image, menuitem=menu_item)

        return menu_item

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])

        for image in uploaded_images:
            MenuItemImage.objects.create(image=image, menuitem=instance)

        return super().update(instance, validated_data)


class MenuItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemImage
        fields = (
            "id",
            "url",
            "image",
            "menuitem",
        )
