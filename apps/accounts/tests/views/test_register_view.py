from django.test import TestCase
from django.urls import reverse


class TestRegistrationForm(TestCase):

    def setUp(self):
        self.register_url = reverse("register")
        return super().setUp()

    def test_GET_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/pages/register.html')
        self.assertTrue(response.has_header("Content-Type"))

    def test_POST_register_view(self):
        pass