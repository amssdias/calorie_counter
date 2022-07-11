from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User


class TestDailyUserFoodStatusView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing123"
        )
        cls.list_url = reverse("foods:food_consumed_daily_list")
        return super().setUpTestData()

    def test_GET_daily_user_food_status_list_view_status_code(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_GET_daily_user_food_status_list_view_template_used(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.list_url)
        self.assertTemplateUsed(response, "foods/daily_user_food_stats_list.html")

    def test_GET_daily_user_food_status_list_view_not_authenticated(self):
        response = self.client.get(self.list_url, follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
