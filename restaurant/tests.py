import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from restaurant.models import Restaurant
from employee.models import Employee


# creating restaurant test
@pytest.mark.django_db
def test_create_restaurant():
    client = APIClient()

    user = User.objects.create_user(username='admin', password='admin123')
    employee = Employee.objects.create(user=user, department="admin")

    client.force_authenticate(user=user)


    data = {
        "name": "Test Restaurant",
        "address": "123 Test St"
    }

    response = client.post('/api/restaurants/', data, format='json')

    assert response.status_code == 201
    assert Restaurant.objects.filter(name="Test Restaurant").exists()


# getting restaurant list test
@pytest.mark.django_db
def test_get_restaurant_list():
    client = APIClient()

    user = User.objects.create_user(username='admin', password='admin123')
    employee = Employee.objects.create(user=user, department="admin")

    client.force_authenticate(user=user)

    Restaurant.objects.create(name="Test Restaurant 1", address="123 Test St")
    Restaurant.objects.create(name="Test Restaurant 2", address="456 Another St")

    response = client.get('/api/restaurants/')


    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['name'] == "Test Restaurant 1"
    assert response.data[1]['name'] == "Test Restaurant 2"
