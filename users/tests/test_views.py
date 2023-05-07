# AAA - arrange, act, assert
from django.urls import reverse
from pprint import pprint as pp


def test_registration_page(client):
    # arrange
    url = reverse('users:registration')

    # act
    response = client.get(url)

    # assert
    assert response.status_code == 200
    assert '<h1>Registration Form</h1>' in response.content.decode('UTF-8')


def test_login_page(client):
    url = reverse('users:login')

    response = client.get(url)

    assert response.status_code == 200
    assert '<h1>Login Form</h1>' in response.content.decode('UTF-8')


def test_register_user(client, db, django_user_model):
    url = reverse('users:registration')
    data = {
        'email': 'testUser@test.com',
        'fullname': 'Jacek S',
        'is_instructor': False,
        'password': 'midas',
        'password_confirmation': 'midas'
    }
    redirect = client.post(url, data=data)
    user = django_user_model.objects.get(email=data['email'])

    assert redirect.status_code == 302
    assert user.fullname == data['fullname']
    assert user.is_instructor == data['is_instructor']

    response = client.get(redirect.url)

    assert response.status_code == 200
    assert 'You are registered. Please login. Your login: testUser@test.com' in response.content.decode('UTF-8')

