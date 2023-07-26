from django.db import models
from django.core import validators


class MenuCategory(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, blank=False, null=False)
    weight = models.IntegerField(default=0)
    manufacture_date = models.DateField(auto_now_add=True, blank=False)
    expiration_date = models.DateField(blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True,)
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, validators=[validators.MinValueValidator(0)])
    image = models.ImageField(upload_to="images/menuitem/", null=True, blank=True)

    def __str__(self):
        return self.name


class MenuItemImage(models.Model):
    objects = models.Manager()
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="images/menuitem/")

    def __str__(self):
        return self.menuitem.name
