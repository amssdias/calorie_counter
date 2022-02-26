from django.test import TestCase

from apps.accounts.models.profile import Profile
from apps.accounts.models.user import User


class TestUserModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="Test", email="test@testing.com", password="testing1234")

    def test_profile_was_created(self):
        self.assertTrue(Profile.objects.get(user=self.user))
        