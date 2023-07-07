from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    isdeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Branches(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    opening_time = models.DateTimeField(default=timezone.now)
    closing_time = models.DateTimeField(default=timezone.now)
    manager_name = models.CharField(max_length=255)
    location_url = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    branches_id = models.ForeignKey(Branches, on_delete=models.CASCADE, default=None)
    product_id = models.IntegerField(default=None)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=None)
    arrivalDate = models.DateTimeField(default=timezone.now)
    expirationDate = models.DateTimeField(default=timezone.now)
    supplier = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    price = models.CharField(max_length=100, default='0')
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.supplier