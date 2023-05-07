from django.contrib.auth.models import Permission
from django.urls import reverse


def test_create_course_non_instructor(client, user):
    url = reverse('courses:course-create')
    client.force_login(user)

    response = client.get(url)

    assert response.status_code == 403


def test_create_course_instructor(client, user):
    url = reverse('courses:course-create')
    permission = Permission.objects.get(codename='add_course')
    user.user_permissions.add(permission)
    user.save()

    client.force_login(user)

    response = client.get(url)

    assert response.status_code == 200
    assert '<h1>Create/Update:</h1>' in response.content.decode('UTF-8')
