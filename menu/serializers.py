from rest_framework import serializers
from .models import MenuCategory,MenuItem,Product,MenuItemImage


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = (
            'id',
            'name',
            'url',
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'weight',
            'manufacture_date',
            'expiration_date',
        )

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=MenuCategory.objects.all())

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(required=False),
        allow_empty=True,
        write_only=True,
        required=False,
    )

    class Meta:
        model = MenuItem
        fields =(
            'category',
            'products',
            'name',
            'description',
            'price',
            'uploaded_images'
        )


def create(self, validated_data):
    uploaded_images = validated_data.pop("uploaded_images", [])
    products_data = validated_data.pop("products", [])

    menu_item = MenuItem.objects.create(**validated_data)

    menu_item.products.set(products_data)  # Use set() to assign many-to-many relationship

    for image in uploaded_images:
        MenuItemImage.objects.create(image=image, menuitem=menu_item)

    return menu_item


def update(self, instance, validated_data):
    uploaded_images = validated_data.pop("uploaded_images", [])
    products_data = validated_data.pop("products", [])

    instance = super().update(instance, validated_data)

    instance.products.set(products_data)  # Use set() to assign many-to-many relationship

    for image in uploaded_images:
        MenuItemImage.objects.create(image=image, menuitem=instance)

    return instance

class MenuItemImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItemImage
        fields = (
            "id",
            "url",
            "image",
            "menuitem",
        )

