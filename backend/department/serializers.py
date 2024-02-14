from rest_framework.serializers import ModelSerializer

from department.models import Department, Employees


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name',)


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'department', 'chief', 'name', 'salary',)