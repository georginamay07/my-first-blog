
from django.test import TestCase
from django.http import HttpRequest
from .models import Post
from .models import CV 
from .models import Work
from .models import Education
from django.urls import resolve
from blog.views import cv
from blog.views import homepage

class PageTest(TestCase):

    def test_root_url_resolves_to_cv_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_url_resolves_to_cv_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv)

    def test_can_save_CV_request(self):
        self.client.post('/admin/blog/cv/1/change/', data={'email': 'GMC851@student.bham.ac.uk'})
        self.assertEqual(CV.objects.count(), 1)
        new_item = CV.objects.first()
        self.assertEqual(new_item.text, '07496879858')

    def test_redirects_after_CV(self):
        response = self.client.post('/admin/blog/cv/1/change/', data={'email': 'GMC851@student.bham.ac.uk'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/')
        self.assertEqual(CV.objects.count(), 0)

    def test_displays_all_CV_items(self):
        CV.objects.create(email='GMC851@student.bham.ac.uk')
        CV.objects.create(mobile='07496879858')

        response = self.client.get('/cv/')

        self.assertIn('GMC851@student.bham.ac.uk', response.content.decode())
        self.assertIn('07496879858', response.content.decode())
