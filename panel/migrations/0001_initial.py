# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Panel'
        db.create_table('panel_panel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('panelId', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('margin', self.gf('django.db.models.fields.FloatField')()),
            ('active_area', self.gf('django.db.models.fields.FloatField')()),
            ('active_margin', self.gf('django.db.models.fields.FloatField')()),
            ('stroke_lead', self.gf('django.db.models.fields.FloatField')()),
            ('stroke_end', self.gf('django.db.models.fields.FloatField')()),
            ('full_stroke', self.gf('django.db.models.fields.FloatField')()),
            ('voltage', self.gf('django.db.models.fields.FloatField')()),
            ('solette_spacing', self.gf('django.db.models.fields.FloatField')()),
            ('solette_length', self.gf('django.db.models.fields.FloatField')()),
            ('initial_stroke', self.gf('django.db.models.fields.FloatField')()),
            ('strokePosition', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('panel', ['Panel'])


    def backwards(self, orm):
        # Deleting model 'Panel'
        db.delete_table('panel_panel')


    models = {
        'panel.panel': {
            'Meta': {'object_name': 'Panel'},
            'active_area': ('django.db.models.fields.FloatField', [], {}),
            'active_margin': ('django.db.models.fields.FloatField', [], {}),
            'full_stroke': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_stroke': ('django.db.models.fields.FloatField', [], {}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'margin': ('django.db.models.fields.FloatField', [], {}),
            'panelId': ('django.db.models.fields.TextField', [], {}),
            'solette_length': ('django.db.models.fields.FloatField', [], {}),
            'solette_spacing': ('django.db.models.fields.FloatField', [], {}),
            'strokePosition': ('django.db.models.fields.FloatField', [], {}),
            'stroke_end': ('django.db.models.fields.FloatField', [], {}),
            'stroke_lead': ('django.db.models.fields.FloatField', [], {}),
            'voltage': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['panel']