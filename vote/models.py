from django.contrib.auth.models import User
from django.db import models

from employee.models import Employee
from menu.models import Menu

class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'menu')

    def __str__(self):
        return f'{self.employee.user.username} voted for menu {self.menu.id} on {self.created_at}'
