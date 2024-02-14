from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Employees(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='stuff')
    chief = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinates')
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self) -> str:
        return self.name
