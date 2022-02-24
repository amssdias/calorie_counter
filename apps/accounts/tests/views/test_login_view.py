from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User


class TestLoginView(TestCase):

    def setUp(self):
        self.register_url = reverse("login")
        return super().setUp()

    def test_GET_login_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pages/login.html")

    def test_POST_login_view(self):
        user = User(email="test@testing.com")
        user.set_password("password123")
        user.save()
        payload = {
            "email": "test@testing.com",
            "password": "password123",
        }
        response = self.client.post(self.register_url, payload, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_POST_login_view_inactive_user(self):
        user = User(email="test@testing.com")
        user.set_password("password123")
        user.save()
        payload = {
            "email": "test@testing.com",
            "password": "passwor3",
        }
        response = self.client.post(self.register_url, payload, follow=True)

        # By default django sends a status code of 200 for invalid credentials or some error to login
        # Therefore we can check for some errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pages/login.html")
        self.assertTrue("invalid_login" in response.context_data["form"].error_messages)
        self.assertFalse(response.context_data["form"].is_valid())

    def test_POST_login_view_wrong_password(self):
        user = User(email="test@testing.com")
        user.set_password("password123")
        user.is_active = True
        user.save()
        payload = {
            "email": "test@testing.com",
            "password": "passwor3",
        }
        response = self.client.post(self.register_url, payload, follow=True)

        # By default django sends a status code of 200 for invalid credentials or some error to login
        # Therefore we can check for some errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pages/login.html")
        self.assertTrue("invalid_login" in response.context_data["form"].error_messages)
        self.assertFalse(response.context_data["form"].is_valid())
