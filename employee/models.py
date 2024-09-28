from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('developer', 'Developer'),
        ('tester', 'Tester'),
        ('designer', 'Designer'),
        ('devops', 'DevOps'),
        ('business analysis', 'Business Analysis'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.TextField(max_length=20, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.get_department_display()})"