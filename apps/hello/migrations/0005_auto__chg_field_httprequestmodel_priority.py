# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HttpRequestModel.priority'
        db.alter_column(u'hello_httprequestmodel', 'priority', self.gf('django.db.models.fields.IntegerField')(max_length=1))

    def backwards(self, orm):

        # Changing field 'HttpRequestModel.priority'
        db.alter_column(u'hello_httprequestmodel', 'priority', self.gf('django.db.models.fields.CharField')(max_length=7))

    models = {
        u'hello.dbactions': {
            'Meta': {'object_name': 'DbActions'},
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'hello.httprequestmodel': {
            'Meta': {'object_name': 'HttpRequestModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
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