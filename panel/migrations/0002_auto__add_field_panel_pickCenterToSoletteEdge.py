# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Panel.pickCenterToSoletteEdge'
        db.add_column('panel_panel', 'pickCenterToSoletteEdge',
                      self.gf('django.db.models.fields.FloatField')(default=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Panel.pickCenterToSoletteEdge'
        db.delete_column('panel_panel', 'pickCenterToSoletteEdge')


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
            'pickCenterToSoletteEdge': ('django.db.models.fields.FloatField', [], {}),
            'solette_length': ('django.db.models.fields.FloatField', [], {}),
            'solette_spacing': ('django.db.models.fields.FloatField', [], {}),
            'strokePosition': ('django.db.models.fields.FloatField', [], {}),
            'stroke_end': ('django.db.models.fields.FloatField', [], {}),
            'stroke_lead': ('django.db.models.fields.FloatField', [], {}),
            'voltage': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['panel']