from django.db import models


class MenuCategory(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    photo = models.ImageField(upload_to='photos/menucategory', blank=True, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, blank=False, null=False,unique=True)
    weight = models.IntegerField(default=0)
    arrival_date = models.DateField(blank=False, null=False)
    quantity = models.DecimalField(max_digits=3, decimal_places=0, default=1)
    min_limit = models.DecimalField(max_digits=3, decimal_places=0, default=1)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Products)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    image = models.ImageField(upload_to="images/menuitem/", null=True, blank=True)
    quantity = models.DecimalField(max_digits=3, decimal_places=0, default=1)
    min_limit = models.DecimalField(max_digits=3, decimal_places=0, default=1)
    arrivalDate = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.name
