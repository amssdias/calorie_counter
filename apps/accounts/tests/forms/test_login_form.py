from django.test import TestCase

from apps.accounts.forms import LoginForm
from apps.accounts.models.user import User


class TestLoginForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testing", email="test@testing.com", password="1234Testing")
        cls.data = {
            "username": "testing@gmail.com",
            "password": "1234Testing",
        }
    
    def test_form_valid(self):
        data = {
            "username": "test@testing.com",
            "password": "1234Testing"
        }
        login_form = LoginForm(data=data)
        self.assertTrue(login_form.is_valid())

    def test_form_invalid_password(self):
        data = {
            "username": "test@testing.com",
            "password": "Testing"
        }
        login_form = LoginForm(data=data)
        self.assertFalse(login_form.is_valid())

    def test_form_invalid_email(self):
        data = {
            "username": "no_email@testing.com",
            "password": "testing123"
        }
        login_form = LoginForm(data=data)
        self.assertFalse(login_form.is_valid())

    def test_form_invalid_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        data = {
            "username": "no_email@testing.com",
            "password": "testing123"
        }
        login_form = LoginForm(data=data)
        self.assertFalse(login_form.is_valid())
    