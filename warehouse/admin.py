from django.contrib import admin
from .models import Branches, Ingredients, ReadyProducts


admin.site.register(Branches)
admin.site.register(Ingredients)
admin.site.register(ReadyProducts)
