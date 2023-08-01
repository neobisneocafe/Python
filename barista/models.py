from django.db import models
import menu.models
import stuff.models
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
    order_contents = models.ManyToManyField(menu.models.MenuItem)

    def __str__(self):
        return self.order_contents.name


class Menu(models.Model):
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_schedule = models.ForeignKey(stuff.models.WorkSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

