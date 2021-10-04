from django.test import TestCase
from .forms import NewsForm


class TestNewsForm(TestCase):

    def test_form_required_fields(self):
        form = NewsForm({'title': '',
                         'description': '',
                         'image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_form_non_required_fields(self):
        form = NewsForm({'title': 'Test title',
                         'description': 'test description',
                         'image': ''})
        self.assertTrue(form.is_valid())
