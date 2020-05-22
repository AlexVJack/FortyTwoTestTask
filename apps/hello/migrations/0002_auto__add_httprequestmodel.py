# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequestModel'
        db.create_table(u'hello_httprequestmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'hello', ['HttpRequestModel'])


    def backwards(self, orm):
        # Deleting model 'HttpRequestModel'
        db.delete_table(u'hello_httprequestmodel')


    models = {
        u'hello.httprequestmodel': {
            'Meta': {'object_name': 'HttpRequestModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
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