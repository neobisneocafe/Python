from django.db import models
from django.utils import timezone
import menu.models


class Branches(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    opening_time = models.DateTimeField(default=timezone.now)
    closing_time = models.DateTimeField(default=timezone.now)
    location_url = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class ReadyProducts(models.Model):
    menu_item = models.ForeignKey(menu.models.MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    min_limit = models.IntegerField(default=1)
    arrivalDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.menu_item


class Ingredients(models.Model):
    products = models.ForeignKey(menu.models.Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    min_limit = models.IntegerField(default=1)
    arrivalDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.products
