from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from employees.models import Employee


class EmployeeAPITests(APITestCase):

    def setUp(self):
        self.employee_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "department": "Engineering",
            "role": "Developer",
        }

    def test_create_employee(self):
        response = self.client.post("/api/employees/", self.employee_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee_duplicate_email(self):
        Employee.objects.create(**self.employee_data)
        response = self.client.post("/api/employees/", self.employee_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        Employee.objects.create(**self.employee_data)
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_retrieve_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.get(f"/api/employees/{employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_employee_not_found(self):
        response = self.client.get("/api/employees/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        updated_data = {
            "name": "John Updated",
            "email": "john@example.com",
            "department": "HR",
            "role": "Manager",
        }
        response = self.client.put(
            f"/api/employees/{employee.id}/",
            updated_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.delete(f"/api/employees/{employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
