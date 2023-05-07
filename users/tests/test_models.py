import pytest


@pytest.mark.slow
def test_create_user(user, django_user_model):
    users = django_user_model.objects.filter(email='testUser@gmail.com')

    assert len(users) == 1
    assert users.first().fullname == 'Janusz Kowalski'


# @pytest.mark.skip(reason='WIP')
@pytest.mark.smoke
@pytest.mark.slow
def test_change_password(user):
    user.set_password('topSecret')
    assert user.check_password('topSecret') is True
