from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from mock import Mock
from ..middleware import CustomMiddleware
from ..models import HttpRequestModel, PersonInfo


class ViewTests(TestCase):
    def test_about_using_template(self):
        "tests that correct templates are used"
        PersonInfo.objects.create(name='John')
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response,
                                'hello/personinfo.html')
        response = self.client.get(reverse('requests'))
        self.assertTemplateUsed(response,
                                'hello/httprequestmodel_list.html')

    def test_homepage(self):
        "Tests response code 200"
        PersonInfo.objects.create(name='John')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)

    def test_one_entry(self):
        "Tests if field-name presented on response page"
        response = self.client.get('/')
        self.assertContains(response, 'Oleksandr')
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


class PersonUpdateTest(TestCase):
    def test_update_person(self):
        "testing response and correct value sent from form to db"
        person = PersonInfo.objects.create(name='John')
        # This is unknown user and response should be 302
        response = self.client.post(
            reverse('update', kwargs={'pk': person.id}))
        self.assertEqual(response.status_code, 302)
        # Authentication
        c = Client()
        c.login(username='admin', password='admin')
        # This is authorized user and response should be 200
        response = c.post(
            reverse('update', kwargs={'pk': person.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(person.name, 'John')
