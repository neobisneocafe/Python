from django.db import models
from django.utils import timezone

class MenuCategory(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    photo = models.ImageField(upload_to='photos/menucategory', blank=True, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, blank=False, null=False)
    weight = models.IntegerField(default=0)
    arrival_date = models.DateField(blank=False, null=False)
    quantity = models.IntegerField(default=1)
    min_limit = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Products)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    image = models.ImageField(upload_to="images/menuitem/", null=True, blank=True)
    quantity = models.IntegerField(default=1)
    min_limit = models.IntegerField(default=1)
    arrivalDate = models.DateField(blank=False, null=False,default=timezone.now)

    def __str__(self):
        return self.name