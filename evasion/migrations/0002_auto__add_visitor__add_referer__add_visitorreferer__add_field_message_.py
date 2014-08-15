# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Visitor'
        db.create_table(u'evasion_visitor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('hits', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'evasion', ['Visitor'])

        # Adding model 'Referer'
        db.create_table(u'evasion_referer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('hits', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'evasion', ['Referer'])

        # Adding model 'VisitorReferer'
        db.create_table(u'evasion_visitorreferer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visitor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['evasion.Visitor'])),
            ('referer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['evasion.Referer'])),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'evasion', ['VisitorReferer'])

        # Adding field 'Message.visitor'
        db.add_column(u'evasion_message', 'visitor',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', null=True, to=orm['evasion.Visitor']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Visitor'
        db.delete_table(u'evasion_visitor')

        # Deleting model 'Referer'
        db.delete_table(u'evasion_referer')

        # Deleting model 'VisitorReferer'
        db.delete_table(u'evasion_visitorreferer')

        # Deleting field 'Message.visitor'
        db.delete_column(u'evasion_message', 'visitor_id')


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
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'visitor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'null': 'True', 'to': u"orm['evasion.Visitor']"})
        },
        u'evasion.referer': {
            'Meta': {'ordering': "['host']", 'object_name': 'Referer'},
            'hits': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'host': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'evasion.visitor': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Visitor'},
            'hits': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'evasion.visitorreferer': {
            'Meta': {'object_name': 'VisitorReferer'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'referer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['evasion.Referer']"}),
            'visitor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['evasion.Visitor']"})
        }
    }

    complete_apps = ['evasion']