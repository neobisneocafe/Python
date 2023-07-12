from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.conf import settings


class SuperUser(BaseUserManager):
    def create_superuser(self, name, phone, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("role", 'admin_panel')

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")
        if other_fields.get("role") != 'admin_panel':
            raise ValueError("Superuser must be assigned to role=admin_panel")
        return self.create_user(name=name, phone=phone, password=password, **other_fields)

    def create_user(self, name, phone, password=None, **extra_fields):
        if self.model.objects.filter(phone=phone).exists():
            raise ValueError("Такой номер уже существует")

        user = self.model(
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    role_choices = [
        ('client', 'client'),
        ('barista', 'barista'),
        ('waiter', 'waiter'),
        ('admin_panel', 'admin_panel'),
    ]
    role = models.CharField(max_length=255, choices=role_choices, null=True, default='client')
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, unique=True)
    is_verified = models. BooleanField(default=False)
    birthday = models.DateField(null=True, blank=True)
    bonuses = models.IntegerField(default=0)
    order_history = models.CharField(max_length=255)
    is_client = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=4)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['name']

    objects = SuperUser()

    def __str__(self) -> str:
        return "{} - {}".format(self.name, self.phone)


class Cart(models.Model):
    total_price = models.FloatField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pk}"
