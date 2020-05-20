from django.test import TestCase
from django.core.urlresolvers import reverse
from hello.models import PersonInfo


class ViewTests(TestCase):
    def test_about_using_template(self):
        "Tests that correct page is rendered"
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response,
                                'hello/personinfo_list.html')

    def test_homepage(self):
        "Tests response code 200 of mainpage"
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_one_field(self):
        "Tests if field-name presented on response page"
        PersonInfo.objects.create(name='John')
        response = self.client.get('/')
        self.assertContains(response, 'John')


class TestModels(TestCase):
    def test_model_str(self):
        "This shows if model returns normal str"
        men = PersonInfo.objects.create(name="John")
        self.assertEqual(str(men), "John")


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)
