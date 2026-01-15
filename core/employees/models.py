from django.db import models

# Create your models here.
from django.core.validators import EmailValidator


class Employee(models.Model):
    """
    Employee model for managing company employees.
    The `id` field is automatically created by Django
    as an auto-incrementing primary key.
    """

    name = models.CharField(max_length=255)
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator()],
    )
    department = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.name} ({self.email})"
