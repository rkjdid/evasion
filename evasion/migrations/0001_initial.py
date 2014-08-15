# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'evasion_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=60)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('date_reservation', self.gf('django.db.models.fields.DateField')()),
            ('date_filled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('message_sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_message', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 15, 0, 0))),
        ))
        db.send_create_signal(u'evasion', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'evasion_message')


    models = {
        u'evasion.message': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Message'},
            'date_filled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_message': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 15, 0, 0)'}),
            'date_reservation': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'message_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['evasion']