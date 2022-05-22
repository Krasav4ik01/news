from urllib import response
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse, resolve
from .models import *
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser, User
from .views import *

# Create your tests here.

class YourTestClass(TestCase):
    # def test_something(self):
    #     self.assertEqual(1+1,2)
    # def test_something_that_will_pass(self):
    #     self.assertFalse(False)

    # def test_something_that_will_fail(self):
    #     self.assertTrue(False)
        
    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
        
    def test_setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')

    def test_list(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func, main)


    def test_model(self):
        name = Labours.objects.create(name="Some Name")
        labout = Labours.objects.create(labour="Some labour")
        self.assertEqual(str(name), 'Some Name')
        
        
    def test_url_exists(self):
        response = self.client.get("/new/")
        self.assertEqual(response.status_code, 200)
        
        
        
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    # def setUp(self):
    #     self.client = Client()
    #     self.list_url = reverse('list')
    #     self.detail_url = reverse('detail', args=[''])
    
    
    
    
    # def test_project(self):
    #     response = self.client.get(self.list_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'main/main.html')
        
        
    # def test_project_detail(self):
    #     response = self.client.get(self.detail_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'main/new.html')

    # def test_objects(self):
    #     objects = Heroes.objects.all()
    #     self.assertRaises(objects)
    # def test_details(self):
    #     # Create an instance of a GET request.
    #     request = self.factory.get('/customer/details')

    #     # Recall that middleware are not supported. You can simulate a
    #     # logged-in user by setting request.user manually.
    #     request.user = self.user

    #     # Or you can simulate an anonymous user by setting request.user to
    #     # an AnonymousUser instance.
    #     request.user = AnonymousUser()

    #     # Test my_view() as if it were deployed at /customer/details
    #     response = main(request)
    #     # Use this syntax for class-based views.
    #     response = main.as_view()(request)
    #     self.assertEqual(response.status_code, 200)