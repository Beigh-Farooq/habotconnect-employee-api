from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from .models import Employee
from .serializers import EmployeeSerializer

def employee_page(request):
    return render(request, "employees/employees_list.html")

# Create & List Employees
@api_view(['GET', 'POST'])
def employee_list_create(request):
    """
    GET: List employees (with filtering & pagination)
    POST: Create a new employee
    """

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # GET request
    queryset = Employee.objects.all()

    # Filtering
    department = request.query_params.get('department')
    role = request.query_params.get('role')

    if department:
        queryset = queryset.filter(department=department)
    if role:
        queryset = queryset.filter(role=role)

    # Pagination (10 per page)
    paginator = Paginator(queryset, 10)
    page_number = request.query_params.get('page', 1)
    page = paginator.get_page(page_number)

    serializer = EmployeeSerializer(page, many=True)

    return Response({
        "count": paginator.count,
        "total_pages": paginator.num_pages,
        "current_page": page.number,
        "results": serializer.data
    })


# Retrieve, Update, Delete Employee
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(
            {"detail": "Employee not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(
            employee,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        employee.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
