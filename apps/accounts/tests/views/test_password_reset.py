from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User


class TestPasswordResetView(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="testing", email="testing@gmail.com", password="1234test")
        cls.reset_password_url = reverse("accounts:reset_password_custom")
        return super().setUpTestData()

    def test_GET_password_reset_view(self):
        response = self.client.get(self.reset_password_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/password-reset/password_reset_form.html")


    def test_POST_password_reset_view(self):
        payload = {
            "email": "testing@gmail.com"
        }
        response = self.client.post(self.reset_password_url, payload, follow=True, secure=True)
        self.assertEqual(response.redirect_chain[0][0], reverse("accounts:login"))
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_POST_password_reset_view(self):
        payload = {
            "email": "testing_wrong@gmail.com"
        }
        response = self.client.post(self.reset_password_url, payload, follow=True, secure=True)
        self.assertFalse(response.context_data["form"].is_valid())
        self.assertEqual(response.status_code, 400)
