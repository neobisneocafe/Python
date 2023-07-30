from django.db import models
from django.utils import timezone

import menu.models
from menu.models import MenuItem
from users.models import User


class Order(models.Model):
    STATUS_CHOICES = (
        ('новый', 'Новый'),
        ('в_процессе', 'В процессе'),
        ('готово', 'Готово'),
        ('отменено', 'Отменено'),
        ('оплачено', 'Оплачено'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='новый')
    is_takeaway = models.BooleanField(default=False)
    table = models.IntegerField(null=True, default=None)
    order_contents = models.ForeignKey(menu.models.MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_contents


class Menu(models.Model):
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_schedule = models.CharField(max_length=255)

    def __str__(self):
        return self.user


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    @classmethod
    def generate_notification(cls):
        orders = Order.objects.filter(status='new')
        for order in orders:
            time_diff = timezone.now() - order.created_at
            minutes_passed = time_diff.total_seconds() // 60
            if minutes_passed >= 10:
                message = f"Напоминание! Примите заказ  #{order.id}"
                notification = cls.objects.create(profile=order.profile, message=message)

    def __str__(self):
        return self.user


class WorkSchedule(models.Model):
    DAY_CHOICES = (
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_weekend = models.BooleanField(default=False)

    def __str__(self):
        return self.user
