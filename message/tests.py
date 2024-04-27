from django.test import SimpleTestCase
from django.urls import reverse  # convert name of url to real url
# Create your tests here.

class MessagePageTests(SimpleTestCase):
    def test_url_exist(self):
        response = self.client.get("/message/") # http request in message addres
        self.assertEqual(response.status_code, 200) # response.status == 200 ? y or n

    def test_url_available_by_name(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code , 200)


    def test_template_name(self):
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response , 'home.html') # test that name of message's template is home.html or not

    def test_template_content(self):
        response = self.client.get(reverse('message'))
        self.assertContains(response , '<h1>welcome to home page</h1>')