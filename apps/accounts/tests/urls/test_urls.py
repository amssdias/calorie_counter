from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LogoutView

from apps.accounts.views import (
    RegisterView, 
    CustomLoginView, 
    ActivateAccountView, 
    CustomPasswordResetView, 
    CustomPasswordResetConfirmView,
    )


class TestUrls(TestCase):

    def test_register_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_activate_account_url_resolves(self):
        url = reverse('accounts:activate_account', kwargs={'uidb64': 'MTE', 'token': 'abcde123'})
        self.assertEqual(resolve(url).func.view_class, ActivateAccountView)

    def test_login_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, CustomLoginView)

    def test_logout_url_resolves(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_password_reset_url_resolves(self):
        url = reverse('accounts:reset_password_custom')
        self.assertEqual(resolve(url).func.view_class, CustomPasswordResetView)
    
    def test_password_reset_confirm_url_resolves(self):
        url = reverse('accounts:password_reset_confirm', kwargs={'uidb64': 'MTE', 'token': 'abcde123'})
        self.assertEqual(resolve(url).func.view_class, CustomPasswordResetConfirmView)
