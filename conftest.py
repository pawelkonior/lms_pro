import pytest


@pytest.fixture
def user(db, django_user_model):
    """Create a test user instance for testing purposes.

     This fixture creates a test user with a specified email, fullname, and password. It
     relies on the 'db' fixture provided by pytest-django to access the database and the
     'django_user_model' fixture to access the User model.

     Args:
         db: A pytest fixture that enables test access to the Django database.
         django_user_model: A pytest fixture that returns the User model used in the project.

     Returns:
         A User instance with the specified email, fullname, and password.
     """

    return django_user_model.objects.create_user(
        email='testUser@gmail.com',
        fullname='Janusz Kowalski',
        password='Dworczyk123'
    )
