from django.db import models
from datetime import time


class Branch(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    position = models.CharField(max_length=100, blank=False, null=True)
    objects = models.Manager()
    name = models.CharField(max_length=100,blank=False,null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True)
    phone_number = models.CharField(max_length=50,unique=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class WorkSchedule(models.Model):
    objects = models.Manager()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
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