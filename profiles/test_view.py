from django.contrib.auth.models import User
from django.test import TestCase
from .models import UserProfile
from checkout.models import Order


class TestAnonymousViews(TestCase):

    def test_get_profile_page(self):
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")


class TestUserViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        user_profile = UserProfile.objects.create(default_first_name="Test")
        user_profile.save()

        order = Order.objects.create(
                    user_profile=user_profile,
                    full_name="Test",
                    email="Test",
                    phone_number="Test",
                    country="Test",
                    town_or_city="Test",
                    street_address1="Test"
                    )
        order.save()

    def setUp(self):
        self.client.login(username="testuser", password="test")

    def test_get_profile_page(self):
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")


class TestAdminViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser("testadmin", "test@test.com", "test")

    def setUp(self):
        self.client.login(username="testadmin", password="test")

    def test_get_profile_page(self):
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
