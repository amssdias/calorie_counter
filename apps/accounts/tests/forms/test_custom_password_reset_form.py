from django.test import TestCase

from apps.accounts.forms import CustomPasswordResetForm
from apps.accounts.models.user import User


class TestCustomPassowrdResetForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="Test", email="test@testing.com", password="Testing123")
        cls.data = {"email": "test@testing.com"}
        return super().setUpTestData()
    
    def test_form_valid(self):
        custom_password_reset_form = CustomPasswordResetForm(data=self.data)
        self.assertTrue(custom_password_reset_form.is_valid())

    def test_form_invalid_no_data(self):
        custom_password_reset_form_wrong = CustomPasswordResetForm(data={})
        self.assertFalse(custom_password_reset_form_wrong.is_valid())

    def test_form_invalid_email(self):
        custom_password_reset_form_wrong = CustomPasswordResetForm(data={
            "email": "noemail@testing.com"
        })
        self.assertFalse(custom_password_reset_form_wrong.is_valid())