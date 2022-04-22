from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from news_app.views import *

# Create your tests here.
class newsTestCase(TestCase):
    def test_get_news(self):
        client = Client()
        # first request to simulate API check in
        response = client.get('/news/get_news')
        print(response)
        self.assertEqual(response.status_code, 200)
        # second request to test DB check in
        response = client.get('/news/get_news')
        self.assertEqual(response.status_code, 200)
    
    def test_get_news_with_parameter(self):
        client = Client()
        # first request to simulate API check in
        response = client.get('/news/get_news?q=covid')
        self.assertEqual(response.status_code, 200)
        
        # second request to test DB check in
        response = client.get('/news/get_news?q=covid')
        self.assertEqual(response.status_code, 200)