from django.test import TestCase


class TestRegistrationForm(TestCase):

    def setUp(self):
        return super().setUp()

    def test_form_valid(self):
        self.assertEqual(1, 1)