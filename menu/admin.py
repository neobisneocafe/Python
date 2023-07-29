from django.contrib import admin
from .models import MenuItem, MenuCategory, Product, MenuItemImage


class ProductInline(admin.TabularInline):
    model = MenuItem.products.through


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = (
        'name',
        'category',
        'get_products',
        'get_weight',
        'price'
    )

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    get_products.short_description = "Products"

    def get_weight(self, obj):
        weights = {product.name: product.weight for product in obj.products.all()}
        return weights if weights else None

    get_weight.short_description = "Weight"


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuCategory)
admin.site.register(Product)
admin.site.register(MenuItemImage)