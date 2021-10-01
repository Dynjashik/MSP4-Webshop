from django.contrib.auth.models import User
from django.test import TestCase
from .models import SkillCategory, EnvCategory, Product

class TestAnonymousViews(TestCase):

    def setUp(self):
        test_product = Product.objects.create(
             name='Test Product',
             description='test',
             price=1)
        test_product.save()

    def test_get_all_products_anon(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_get_product_details_anon(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    def test_get_add_product_anon(self):
        response = self.client.get("/products/add/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

    def test_get_edit_product_anon(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/edit/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

    def test_can_delete_product_anon(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/delete/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

class TestUserViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("testuser", "test@test.com", "test")

    def setUp(self):
        self.client.login(username="testuser", password="test")
        test_product = Product.objects.create(
             name='Test Product',
             description='test',
             price=1)
        test_product.save()

    def test_get_all_products_user(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_get_product_details_user(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    def test_get_add_product_user(self):
        response = self.client.get("/products/add/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_get_edit_product_user(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/edit/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_can_delete_product_user(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/delete/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

class TestAdminViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser("testadmin", "test@test.com", "test")

    def setUp(self):
        self.client.login(username="testadmin", password="test")
        test_product = Product.objects.create(
             name='Test Product',
             description='test',
             price=1)
        test_product.save()

    def test_get_all_products_admin(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_get_product_details_admin(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    def test_get_add_product_admin(self):
        response = self.client.get("/products/add/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")

    def test_get_edit_product_admin(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/edit/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")

    def test_can_delete_product_admin(self):
        test_product = Product.objects.all()[0]
        response = self.client.get(f'/products/delete/{test_product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")
