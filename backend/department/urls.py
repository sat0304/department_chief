from django.urls import path, include
from rest_framework.routers import DefaultRouter

from department.views import (
    EmployeesViewSet,
    DepartmentViewSet,
)

app_name = 'department'

router = DefaultRouter()

router.register('department', DepartmentViewSet)
router.register('employees', EmployeesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
