from django.test import TestCase

from apps.accounts.forms import LoginForm
from apps.accounts.models.user import User



class TestLoginForm(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testing", email="testing@gmail.com", password="1234Testing")
        self.data = {
            "username": "testing@gmail.com",
            "password": "1234Testing",
        }
        return super().setUp()
    
    def test_form_valid(self):
        # TODO: must pass a request so it can authenticates correctly
        pass
    