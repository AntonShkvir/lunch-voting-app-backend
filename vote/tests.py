import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from menu.models import Menu
from employee.models import Employee
from restaurant.models import Restaurant
from vote.models import Vote

# voting for menu test
@pytest.mark.django_db
def test_vote_for_menu():
    client = APIClient()

    restaurant = Restaurant.objects.create(name="Test Restaurant")


    user = User.objects.create_user(username='voter', password='voter123')
    employee = Employee.objects.create(user=user, department="developer")

    menu = Menu.objects.create(restaurant=restaurant, date="2024-09-30", items="Pizza, Salad")

    client.force_authenticate(user=user)

    data = {
        "menu": menu.id
    }

    response = client.post('/api/votes/', data, format='json')

    assert response.status_code == 201
    assert Vote.objects.filter(employee=employee, menu=menu).exists()

# test voting for menu twice
@pytest.mark.django_db
def test_vote_for_menu_twice():
    client = APIClient()

    restaurant = Restaurant.objects.create(name="Test Restaurant")

    user = User.objects.create_user(username='voter', password='voter123')
    employee = Employee.objects.create(user=user, department="developer")

    menu = Menu.objects.create(restaurant=restaurant, date="2024-09-30", items="Pizza, Salad")

    client.force_authenticate(user=user)

    data = {
        "menu": menu.id
    }

    response = client.post('/api/votes/', data, format='json')
    assert response.status_code == 201

    response = client.post('/api/votes/', data, format='json')

    assert response.status_code == 400
    assert Vote.objects.filter(employee=employee, menu=menu).count() == 1

# test voting without authentication
@pytest.mark.django_db
def test_vote_without_authentication():
    client = APIClient()

    restaurant = Restaurant.objects.create(name="Test Restaurant")

    menu = Menu.objects.create(restaurant=restaurant, date="2024-09-30", items="Pizza, Salad")

    data = {
        "menu": menu.id
    }

    response = client.post('/api/votes/', data, format='json')

    assert response.status_code == 401
