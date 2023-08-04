from django.contrib import admin
from .models import MenuItem, MenuCategory, Products


admin.site.register(MenuItem)
admin.site.register(MenuCategory)
admin.site.register(Products)