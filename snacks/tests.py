# from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class snacks_tests(SimpleTestCase):
    def test_home_status(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_about_status(self):
        url=reverse('about')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_template(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'home.html')
        self.assertTemplateUsed(response,'base.html')
       