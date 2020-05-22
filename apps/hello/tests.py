from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import HttpRequestModel, PersonInfo


class ViewTests(TestCase):
    def test_about_using_template(self):
        "This covers template renders needed page"
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response,
                                'hello/personinfo_list.html')
        response = self.client.get(reverse('requests'))
        self.assertTemplateUsed(response,
                                'hello/httprequestmodel_list.html')

    def test_homepage(self):
        "Tests response code 200 of mainpage"
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)

    def test_one_entry(self):
        "Tests if field-name presented on response page"
        PersonInfo.objects.create(name='John')
        response = self.client.get('/')
        self.assertContains(response, 'John')
        HttpRequestModel.objects.create(method="GET")
        response = self.client.get('/requests/')
        self.assertContains(response, 'GET')


class TestModels(TestCase):
    def test_model_str(self):
        "model returns str"
        men = PersonInfo.objects.create(name="John")
        self.assertEqual(str(men), "John")
