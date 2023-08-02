from django.db import models
from datetime import time


class Branches(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    working_time = models.CharField(max_length=255)
    location_url = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    POSITION_CHOICES = (
        ('бариста', 'бариста'),
        ('официант', 'официант'),
        ('админ', 'админ'),
        ('кассир', 'кассир'),
        ('менеджер', 'менеджер'),
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, unique=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class WorkSchedule(models.Model):
    objects = models.Manager()
    employee = models.ManyToManyField(Employee, blank=True)
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
        return f"{self.employee} - {self.day_of_week}"
