from django.contrib.auth.models import User
from django.test import TestCase
from .models import News


class TestAnonymousViews(TestCase):

    def setUp(self):
        test_news = News.objects.create(
             title='Test News Article',
             description='test description')
        test_news.save()

    def test_get_news_anon(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/news.html")

    def test_get_add_news_anon(self):
        response = self.client.get("/news/add/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

    def test_get_edit_news_anon(self):
        test_news = News.objects.all()[0]
        response = self.client.get(f'/news/edit/{test_news.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

    def test_can_delete_news_anon(self):
        test_news = News.objects.all()[0]
        response = self.client.get(f'/news/delete/{test_news.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")


class TestUserViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("testuser", "test@test.com", "test")

    def setUp(self):
        self.client.login(username="testuser", password="test")
        test_news = News.objects.create(
             title='Test News Article',
             description='test description')
        test_news.save()

    def test_get_news_user(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/news.html")

    def test_get_add_news_user(self):
        response = self.client.get("/news/add/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_get_edit_news_user(self):
        test_news = News.objects.all()[0]
        response = self.client.get(f'/news/edit/{test_news.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_can_delete_news_user(self):
        test_news = News.objects.all()[0]
        response = self.client.get(f'/news/delete/{test_news.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

class TestAdminViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser("testadmin", "test@test.com", "test")

    def setUp(self):
        self.client.login(username="testadmin", password="test")
        test_news = News.objects.create(
             title='Test News Article',
             description='test description')
        test_news.save()

    def test_get_news_admin(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/news.html")

    def test_get_add_news_user_admin(self):
        response = self.client.get("/news/add/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/add_news.html")

    def test_get_edit_news_user(self):
        test_news = News.objects.all()[0]
        response = self.client.get(f'/news/edit/{test_news.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/edit_news.html")

    def test_can_delete_news_user(self):
        test_news = News.objects.all()[0]
        response = self.client.get(f'/news/delete/{test_news.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/news.html")