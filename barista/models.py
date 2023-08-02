from django.db import models
from menu.models import MenuItem
from stuff.models import WorkSchedule
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
    order_content = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.order_content


class Menu(models.Model):
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
