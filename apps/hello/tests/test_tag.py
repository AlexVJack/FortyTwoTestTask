from django.test import TestCase
from django.test import Client

from ..models import PersonInfo
from hello.templatetags.admin_edit_page_link import admin_edit_page_link


class AdminUrlTest(TestCase):
    def test_admin_url(self):
        "testing correct value of edit url"
        # Authentication
        c = Client()
        c.login(username='admin', password='admin')
        # creating one entry
        person = PersonInfo.objects.create(name='John')
        # testing for url
        url = admin_edit_page_link(person)
        self.assertEqual(url, '/admin/hello/personinfo/1/')
