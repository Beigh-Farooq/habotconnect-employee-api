from django.urls import path
from .views import employee_list_create, employee_detail,employee_page

urlpatterns = [
    # Frontend page
    path('', employee_page, name='employee-page'),

    # API endpoints
    path('employees/', employee_list_create),
    path('employees/<int:id>/', employee_detail),
]
