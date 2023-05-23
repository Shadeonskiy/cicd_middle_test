from django.test import TestCase
from .models import Image, Category
from django.urls import reverse

# Create your tests here.
class TestGallery(TestCase):
    def test_gallery_view_success(self):
        path = reverse('main')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_template(self):
        path = reverse('main')
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'gallery.html')

    def test_gallery_view_categories(self):
        category_1 = Category.objects.create(name="category 1")
        category_2 = Category.objects.create(name="category 2")
        category_3 = Category.objects.create(name="category 3")

        path = reverse('main')
        response = self.client.get(path)

        categories = response.context['categories']
        self.assertEqual(len(categories), 3)
        self.assertEqual(set(categories), {category_1, category_2, category_3})

class TestImageDetail(TestCase):
    def test_image_detail_view_success(self):
        category = Category.objects.create(name='category 1')
        image = Image.objects.create(title='image1', image='Component_2.png', created_date="2023-05-23", age_limit=16)
        image.categories.add(category)

        path = reverse('image_detail', args=[image.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
    
    def test_image_detail_view_template(self):
        category = Category.objects.create(name='category 1')
        image = Image.objects.create(title='image1', image='Component_2.png', created_date="2023-05-23", age_limit=16)
        image.categories.add(category)

        path = reverse('image_detail', args=[image.id])
        response = self.client.get(path)

        self.assertTemplateUsed(response, 'image_detail.html')

    def test_image_detail_view_image(self):
        category = Category.objects.create(name='category 1')
        image = Image.objects.create(title='image1', image='Component_2.png', created_date="2023-05-23", age_limit=16)
        image.categories.add(category)
        
        path = reverse('image_detail', args=[image.id])
        response = self.client.get(path)

        self.assertEqual(response.context["image"], image)