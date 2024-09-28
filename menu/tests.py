from unittest import mock

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.utils import timezone

from employee.models import Employee
from restaurant.models import Restaurant
from menu.models import Menu
from vote.models import Vote


# creating menu test
@pytest.mark.django_db
def test_create_menu():
    client = APIClient()

    restaurant = Restaurant.objects.create(name="Test Restaurant", address="123 Test St")

    data = {
        "restaurant": restaurant.id,
        "date": str(timezone.now().date()),
        "items": "test item 1, test item 2, test item 3"
    }

    user = User.objects.create_user(username='employee1', password='password123')
    employee = Employee.objects.create(user=user, department="developer")
    client.force_authenticate(user=user)

    response = client.post('/api/menus/', data, format='json')

    assert response.status_code == 201
    assert Menu.objects.filter(restaurant=restaurant, date=timezone.now().date()).exists()

#  getting current day menu test
@pytest.mark.django_db
def test_get_current_day_menu():
    client = APIClient()

    restaurant = Restaurant.objects.create(name="Test Restaurant", address="123 Test St")
    Menu.objects.create(restaurant=restaurant, date=timezone.now().date(), items="test item 1, test item 2, test item 3")

    user = User.objects.create_user(username='employee1', password='password123')
    employee = Employee.objects.create(user=user, department="developer")
    client.force_authenticate(user=user)

    response = client.get('/api/menus/')

    assert response.status_code == 200
    assert len(response.data) > 0
    assert response.data[0]['items'] == "test item 1, test item 2, test item 3"


# imitating votes and getting test menu with most votes after 13:00
@pytest.mark.django_db
def test_menu_with_most_votes_after_13():
    client = APIClient()


    restaurant = Restaurant.objects.create(name="Test Restaurant", address="123 Test St")
    menu1 = Menu.objects.create(restaurant=restaurant, date=timezone.now().date(), items="Pizza")
    menu2 = Menu.objects.create(restaurant=restaurant, date=timezone.now().date(), items="Pasta")

    user1 = User.objects.create_user(username='employee1', password='password123')
    employee1 = Employee.objects.create(user=user1, department="developer")

    user2 = User.objects.create_user(username='employee2', password='password456')
    employee2 = Employee.objects.create(user=user2, department="tester")

    client.force_authenticate(user=user1)
    Vote.objects.create(employee=employee1, menu=menu1)

    client.force_authenticate(user=user2)
    Vote.objects.create(employee=employee2, menu=menu2)
    Vote.objects.create(employee=employee1, menu=menu2)


    with mock.patch('django.utils.timezone.now', return_value=timezone.now().replace(hour=14)):
        response = client.get('/api/menus/')

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['items'] == "Pasta"
