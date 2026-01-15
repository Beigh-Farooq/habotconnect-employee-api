from django.urls import path
from .views import employee_list_create, employee_detail

urlpatterns = [
    path('employees/', employee_list_create),
    path('employees/<int:id>/', employee_detail),
]
