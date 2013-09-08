# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TextNote'
        db.create_table(u'notes_textnote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'notes', ['TextNote'])

        # Adding model 'ImageNote'
        db.create_table(u'notes_imagenote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'notes', ['ImageNote'])

        # Adding model 'VideoNote'
        db.create_table(u'notes_videonote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'notes', ['VideoNote'])


    def backwards(self, orm):
        # Deleting model 'TextNote'
        db.delete_table(u'notes_textnote')

        # Deleting model 'ImageNote'
        db.delete_table(u'notes_imagenote')

        # Deleting model 'VideoNote'
        db.delete_table(u'notes_videonote')


    models = {
        u'notes.imagenote': {
            'Meta': {'object_name': 'ImageNote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'notes.textnote': {
            'Meta': {'object_name': 'TextNote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'notes.videonote': {
            'Meta': {'object_name': 'VideoNote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['notes']