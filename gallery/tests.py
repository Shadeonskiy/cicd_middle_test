from django.test import TestCase
from .models import Image, Category

# Create your tests here.
class TestGallery(TestCase):
    def test_gallery_view_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'gallery.html')

    def test_gallery_view_categories(self):
        category_1 = Category.objects.create(name="category 1")
        category_2 = Category.objects.create(name="category 2")
        category_3 = Category.objects.create(name="category 3")

        response = self.client.get('/')

        categories = response.context['categories']
        assert len(categories) == 3
        assert set(categories) == {category_1, category_2, category_3}
