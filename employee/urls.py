from django.urls import path
from .views import EmployeeListCreateView, EmployeeRegisterView, EmployeeLoginView

urlpatterns = [
    path('', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('register/', EmployeeRegisterView.as_view(), name='employee-register'),
    path('login/', EmployeeLoginView.as_view(), name='employee-login'),
]