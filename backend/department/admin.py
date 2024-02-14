from django.contrib import admin
from django.utils.safestring import mark_safe
from department import models
from department.models import Department, Employees


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(models.Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'chief', 'name', 'salary',)
