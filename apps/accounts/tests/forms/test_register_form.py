from unittest.mock import patch

from django.test import TestCase

from apps.accounts.forms import RegisterForm
from apps.accounts.models import User
from apps.accounts.models.profile import Profile


class TestRegistrationForm(TestCase):

    def setUp(self):
        self.data = {
            "email": "testing@gmail.com",
            "password1": "1234Testing",
            "password2": "1234Testing",
        }
        self.wrong_data = {
            "email": "testing@gmail.com",
            "password1": "5678Testing",
            "password2": "1234Testing",
        }
        self.register_form = RegisterForm(data=self.data)
        self.register_form_invalid = RegisterForm(data=self.wrong_data)
        return super().setUp()

    def test_form_valid(self):
        self.assertTrue(self.register_form.is_valid())

    def test_form_invalid(self):
        self.assertFalse(self.register_form_invalid.is_valid())
        self.assertTrue(self.register_form_invalid.has_error("password2"))
        self.assertEqual(len(self.register_form_invalid.errors), 1)
        
        register_form_empty = RegisterForm(data={})
        self.assertFalse(register_form_empty.is_valid())

    def test_user_profile_created(self):
        self.register_form.is_valid()
        user = self.register_form.save()
        user_profile = Profile.objects.filter(user=user).exists()
        self.assertTrue(user_profile)

    def test_user_inactive(self):
        self.register_form.is_valid()
        user = self.register_form.save()
        self.assertFalse(user.is_active)
