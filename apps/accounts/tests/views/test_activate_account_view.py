from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.accounts.models.profile import Profile
from apps.accounts.models.user import User
from apps.accounts.utils import generate_token


class TestActivateAccountView(TestCase):

    def setUp(self):
        return super().setUp()

    def test_GET_activate_account_view(self):
        user = User.objects.create_user(username="testing", email="testing@gmail.com", password="Testing123")
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        url = reverse("activate_account", kwargs={
            "uidb64": uid,
            "token": generate_token.make_token(user),
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    
    def test_GET_activate_account_view_wrong_token(self):
        user = User.objects.create_user(username="testing", email="testing@gmail.com", password="Testing123")
        user_1 = User.objects.create_user(username="testing1", email="testing1@gmail.com", password="Testing123")
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        url = reverse("activate_account", kwargs={
            "uidb64": uid,
            "token": generate_token.make_token(user_1),
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, "accounts/email/activation_failed.html")
    
    def test_GET_activate_account_view_wrong_uid(self):
        user = User.objects.create_user(username="testing", email="testing@gmail.com", password="Testing123")
        user_1 = User.objects.create_user(username="testing1", email="testing1@gmail.com", password="Testing123")
        uid = urlsafe_base64_encode(force_bytes(user_1.pk))
        url = reverse("activate_account", kwargs={
            "uidb64": uid,
            "token": generate_token.make_token(user),
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, "accounts/email/activation_failed.html")

    def test_GET_activate_account_view_user_active(self):
        user = User.objects.create_user(username="testing", email="testing@gmail.com", password="Testing123")
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        url = reverse("activate_account", kwargs={
            "uidb64": uid,
            "token": generate_token.make_token(user),
        })
        response = self.client.get(url)
        self.assertTrue(user.is_active)
