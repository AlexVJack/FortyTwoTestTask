from django.test import TestCase
from ..models import DbActions, PersonInfo


class TestSignals(TestCase):
    def test_created(self):
        "tests if after creation we have 'created' in db"
        PersonInfo.objects.create(name='John')
        db_action = DbActions.objects.first()
        action_type = getattr(db_action, 'action_type')
        self.assertEqual(action_type, 'has been created')

    def test_edited(self):
        "tests if after creation we have 'edited' in db"
        person = PersonInfo.objects.create(name='John')
        person.last_name = 'Malkovich'
        person.save()
        db_action = DbActions.objects.last()
        action_type = getattr(db_action, 'action_type')
        self.assertEqual(action_type, 'has been edited')

    def test_deleted(self):
        "tests if after deletion we have 'deleted' in db"
        PersonInfo.objects.create(name='John')
        PersonInfo.objects.first().delete()
        db_action = DbActions.objects.last()
        action_type = getattr(db_action, 'action_type')
        self.assertEqual(action_type, 'has been deleted')
