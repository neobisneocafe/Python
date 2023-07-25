from django.contrib import admin
from .models import MenuItem, MenuCategory, Product, MenuItemImage




admin.site.register(MenuItem)
admin.site.register(MenuCategory)
admin.site.register(Product)
admin.site.register(MenuItemImage)