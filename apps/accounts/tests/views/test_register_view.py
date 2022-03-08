import copy

from django.test import TestCase
from django.urls import reverse
from django.core import mail

from apps.accounts.models.profile import Profile
from apps.accounts.models.user import User


class TestRegistrateView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.register_url = reverse("accounts:register")
        cls.payload = {
            "email": "testing@gmail.com",
            "password1": "randompassword.1234",
            "password2": "randompassword.1234",
        }
        return super().setUpTestData()

    def test_GET_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pages/register.html")
        self.assertTrue(response.has_header("Content-Type"))

    def test_POST_register_view(self):
        response = self.client.post(self.register_url, self.payload, follow=True, secure=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_POST_register_view_email_sent(self):
        self.client.post(self.register_url, self.payload, secure=True)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Activate your account")

    def test_POST_register_view_user_created(self):
        self.client.post(self.register_url, self.payload, secure=True)
        user = User.objects.get(email="testing@gmail.com")
        self.assertTrue(user)

    def test_POST_register_view_profile_created(self):
        self.client.post(self.register_url, self.payload, secure=True)
        user_profile = Profile.objects.filter(user__email="testing@gmail.com").all()
        self.assertTrue(user_profile)
        self.assertEqual(user_profile.count(), 1)

    def test_POST_register_view_unmatching_password(self):
        wrong_password_payload = copy.deepcopy(self.payload)
        wrong_password_payload.update({"password2": "Testing456"})
        response = self.client.post(self.register_url, wrong_password_payload, secure=True)
        self.assertEqual(response.status_code, 400)
        