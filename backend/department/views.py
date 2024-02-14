from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.db.models import Max, Sum
from django.db import connections
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from department.models import Department, Employees
from department.serializers import DepartmentSerializer, EmployeesSerializer


class DepartmentViewSet(ModelViewSet):
    """ Department ViewSet вывод даннах отдела"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeesViewSet(ModelViewSet):
    """ Employees ViewSet вывод даннах персонала"""
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    max_depth = 0

    @action(methods=['GET'], detail=False)
    def get_max_salary(self, request: Request):
        """ Расчет максимальной зарплаты"""
        max_salary = Employees.objects.aggregate(Max("salary"))
        employee_max_salary = Employees.objects.filter(salary__gte=int(max_salary['salary__max'])).first()
        print(connections['default'].queries)
        return Response(employee_max_salary.name)

    def get_subordinates_tree(self, person, depth):
        subordinates = person.subordinates.all()
        if not subordinates:
            depth = 0
            return {'depth': depth, 'name': person.name, 'subordinates': []}
        for subordinate in subordinates:
            depth += 1
            if self.max_depth < depth:
                self.max_depth = depth
            return {
                'depth': depth,
                'name': person.name,
                'subordinates': [self.get_subordinates_tree(subordinate, depth)],
            }
    @action(methods=['GET'], detail=False)
    def get_tree_deep(self, request: Request):
        """ Расчет максимальной иерархии подчиненных"""
        queryset = Employees.objects.all()
        depth_count = 0
        for employee in queryset:
            res = self.get_subordinates_tree(employee, depth_count)
            print(connections['default'].queries)
        return Response(self.max_depth)

    @action(methods=['GET'], detail=False)
    def get_income_department(self, request: Request):
        """ Вывод названия отделa с сумарной максимальной зарплатой"""
        max_salary_department = (
            Employees.objects.values(
                'department').annotate(max_salary_dep=Sum('salary')).order_by())
        income_sum = max_salary_department.aggregate(income_dep_sum=Max('max_salary_dep'))['income_dep_sum']
        income_department = max_salary_department.filter(max_salary_dep__gte=int(income_sum)).order_by()
        department = Department.objects.get(id=income_department[0]['department'])
        print(connections['default'].queries)
        return Response(department.name)

    @action(methods=['GET'], detail=False)
    def get_name_starts_P(self, request: Request):
        """ Вывод имени сотрудника на букву Р и н в конце """
        name_starts_p = Employees.objects.filter(name__startswith='Р').filter(name__endswith='н').values().first()
        print(name_starts_p)
        print(connections['default'].queries)
        return Response(name_starts_p['name'])
