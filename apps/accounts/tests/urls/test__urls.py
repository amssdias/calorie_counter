from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LogoutView

from apps.accounts.views import RegisterView, CustomLoginView, ActivateAccountView


class TestUrls(TestCase):

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_activate_account_url_resolves(self):
        url = reverse('activate_account', kwargs={'uidb64': 'MTE', 'token': 'abcde123'})
        self.assertEqual(resolve(url).func.view_class, ActivateAccountView)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, CustomLoginView)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)
