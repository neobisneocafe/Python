from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False,unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    position = models.CharField(max_length=100,blank=False,null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class WorkSchedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=[
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ])
    start_time = models.TimeField( default='00:00')
    end_time = models.TimeField( default='00:00')

    def __str__(self):
        return f"{self.employee} - {self.day_of_week}"