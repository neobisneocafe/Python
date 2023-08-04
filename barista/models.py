from datetime import time

from django.db import models
from menu.models import MenuItem
from stuff.models import WorkSchedule, Employee


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
    table = models.DecimalField(max_digits=2, decimal_places=0, null=True, default=None)
    order_content = models.ManyToManyField(MenuItem)

    def total_price(self):
        total = 0
        for item in self.order_content.all():
            total += item.price
        return total

    def __str__(self):
        return self.order_content


class Menu(models.Model):
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu


class UserProfile(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=[
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ])
    start_time = models.TimeField(default=time(0, 0))
    end_time = models.TimeField(default=time(0, 0))

    def __str__(self):
        return self.user
