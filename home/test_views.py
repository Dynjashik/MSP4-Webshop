from django.contrib.auth.models import User
from django.test import TestCase

class TestAnonymousViews(TestCase):

    def test_home_page(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

class TestUserViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("testuser", "test@test.com", "test")

    def setUp(self):
        self.client.login(username="testuser", password="test")

    def test_get_homepage(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

class TestAdminViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser("testadmin", "test@test.com", "test")

    def setUp(self):
        self.client.login(username="testadmin", password="test")

    def test_get_homepage(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
