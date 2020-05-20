# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PersonInfo'
        db.create_table(u'hello_personinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('date_of_bearth', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'hello', ['PersonInfo'])


    def backwards(self, orm):
        # Deleting model 'PersonInfo'
        db.delete_table(u'hello_personinfo')


    models = {
        u'hello.personinfo': {
            'Meta': {'object_name': 'PersonInfo'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_bearth': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['hello']