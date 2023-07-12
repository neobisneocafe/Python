from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    work_schedule = models.CharField(max_length=100)
