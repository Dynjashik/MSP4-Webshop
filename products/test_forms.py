from django.test import TestCase
from .forms import ProductForm
from .models import SkillCategory, EnvCategory


class TestProductForm(TestCase):

    def setUp(self):
        # create test categories
        test_skill1 = SkillCategory.objects.create(name='Skill_1')
        test_skill1.save()
        test_skill2 = SkillCategory.objects.create(name='Skill_2')
        test_skill2.save()
        test_env1 = EnvCategory.objects.create(name='Env_1')
        test_env1.save()
        test_env2 = EnvCategory.objects.create(name='Env_2')
        test_env2.save()

    def test_form_required_fields(self):
        form = ProductForm({'name': '',
                            'description': '',
                            'price': '',
                            'skill_category': '',
                            'env_category': '',
                            'image_url': '',
                            'image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('description', form.errors.keys())
        self.assertIn('price', form.errors.keys())
        self.assertIn('skill_category', form.errors.keys())
        self.assertIn('env_category', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')
        self.assertEqual(
            form.errors['skill_category'][0], 'This field is required.')
        self.assertEqual(
            form.errors['env_category'][0], 'This field is required.')

    def test_form_non_required_fields(self):

        skills = SkillCategory.objects.all()
        envs = EnvCategory.objects.all()

        form = ProductForm({'name': 'test',
                            'description': 'test',
                            'price': '1',
                            'skill_category': [skills[0]],
                            'env_category': [envs[0]]})
        self.assertTrue(form.is_valid())

    def test_categories_list_items(self):
        skills = SkillCategory.objects.all()
        envs = EnvCategory.objects.all()
        form = ProductForm({'name': 'test',
                            'description': 'test',
                            'price': '1',
                            'skill_category': skills[0],
                            'env_category': envs[0]})
        self.assertFalse(form.is_valid())
        self.assertIn('skill_category', form.errors.keys())
        self.assertIn('env_category', form.errors.keys())
        self.assertEqual(
            form.errors['skill_category'][0], 'Enter a list of values.')
        self.assertEqual(
            form.errors['env_category'][0], 'Enter a list of values.')
