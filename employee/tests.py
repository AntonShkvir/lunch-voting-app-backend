import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


# registration test
@pytest.mark.django_db
def test_register_user():
    client = APIClient()

    data = {
        "username": "user",
        "password": "1234",
        "department": "business analysis"
    }

    response = client.post('/api/employees/register/', data, format='json')

    assert response.status_code == 201
    assert User.objects.filter(username="user").exists()

# register and token test
@pytest.mark.django_db
def test_login_user():
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="password123")

    login_data = {
        "username": "testuser",
        "password": "password123"
    }

    response = client.post('/api/token/', login_data, format='json')

    assert response.status_code == 200
    assert 'access' in response.data

# invalid register test
@pytest.mark.django_db
def test_login_user_invalid_credentials():
    client = APIClient()

    user = User.objects.create_user(username="added user for testing", password="password123")

    invalid_login_data = {
        "username": "incorrect user",
        "password": "wrongpassword"
    }

    response = client.post('/api/token/', invalid_login_data, format='json')

    assert response.status_code == 401
    assert 'access' not in response.data
