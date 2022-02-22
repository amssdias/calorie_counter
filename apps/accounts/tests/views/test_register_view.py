from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.profile import Profile
from apps.accounts.models.user import User


class TestRegistrateView(TestCase):

    def setUp(self):
        self.register_url = reverse("register")
        return super().setUp()

    def test_GET_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pages/register.html")
        self.assertTrue(response.has_header("Content-Type"))

    def test_POST_register_view(self):
        payload = {
            "email": "testing@gmail.com",
            "password1": "Testing123",
            "password2": "Testing123",
        }
        response = self.client.post(self.register_url, payload, follow=True, secure=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_POST_register_view_wrong_password(self):
        payload = {
            "email": "testing@gmail.com",
            "password1": "Testing456",
            "password2": "Testing123",
        }
        response = self.client.post(self.register_url, payload, secure=True)
        self.assertEqual(response.status_code, 400)

    def test_POST_register_view_user_created(self):
        payload = {
            "email": "testing@gmail.com",
            "password1": "Testing123",
            "password2": "Testing123",
        }
        response = self.client.post(self.register_url, payload, secure=True)
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(email="testing@gmail.com")
        self.assertTrue(user)
        
        user_profile = Profile.objects.filter(user=user).all()
        self.assertEqual(user_profile.count(), 1)