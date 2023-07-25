from rest_framework import serializers

from .models import MenuCategory,MenuItem,Product,MenuItemImage


class MenuItemImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItemImage
        fields = (
            "id",
            "image",
        )

    def get_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None


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
    menu_item_images = serializers.SerializerMethodField()
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = MenuItem
        fields =(
            'id',
            'category',
            'menu_item_images',
            'products',
            'name',
            'description',
            'price',
            'image',
        )
    def get_menu_item_images(self, obj):
        menu_item_images = MenuItemImage.objects.filter(menuitem=obj)
        return MenuItemImageSerializer(menu_item_images, many=True).data

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        products_data = validated_data.pop("products", [])

        image = validated_data.pop("image", None)

        menu_item = MenuItem.objects.create(**validated_data)

        menu_item.products.set(products_data)

        for img in uploaded_images:
            MenuItemImage.objects.create(image=img, menuitem=menu_item)

        if image:
            MenuItemImage.objects.create(image=image, menuitem=menu_item)

        return menu_item

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        products_data = validated_data.pop("products", [])

        image = validated_data.pop("image", None)

        instance = super().update(instance, validated_data)

        instance.products.set(products_data)

        for img in uploaded_images:
            MenuItemImage.objects.create(image=img, menuitem=instance)

        if image:
            MenuItemImage.objects.create(image=image, menuitem=instance)

        return instance