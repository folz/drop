# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ImageNote.actual_image'
        db.add_column(u'notes_imagenote', 'actual_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'ImageNote.image'
        db.alter_column(u'notes_imagenote', 'image', self.gf('django.db.models.fields.TextField')(default=''))

    def backwards(self, orm):
        # Deleting field 'ImageNote.actual_image'
        db.delete_column(u'notes_imagenote', 'actual_image')


        # Changing field 'ImageNote.image'
        db.alter_column(u'notes_imagenote', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

    models = {
        u'notes.imagenote': {
            'Meta': {'object_name': 'ImageNote'},
            'actual_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {}),
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