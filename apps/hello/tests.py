from django.test import TestCase
from django.core.urlresolvers import reverse
from mock import Mock
from .models import HttpRequestModel, PersonInfo
from .middleware import CustomMiddleware


class ViewTests(TestCase):
    '''This covers template renders needed page'''
    def test_about_using_template(self):
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


class TestMiddleware(TestCase):
    def test_requestProcessing(self):
        "if middleware responds"
        self.middleware = CustomMiddleware()
        self.request = Mock()
        self.request.session = {}
        response = self.middleware.process_request(self.request)
        self.assertIsNone(response)
