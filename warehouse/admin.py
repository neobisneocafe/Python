from django.contrib import admin
from .models import Branches, Warehouse, WarehouseCategory


admin.site.register(Branches)
admin.site.register(Warehouse)
admin.site.register(WarehouseCategory)
