# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Panel.conveyorHeadPosition'
        db.delete_column('panel_panel', 'conveyorHeadPosition')

        # Adding field 'Panel.conveyorEnd'
        db.add_column('panel_panel', 'conveyorEnd',
                      self.gf('django.db.models.fields.FloatField')(default=655),
                      keep_default=False)

        # Adding field 'Panel.pickPosition'
        db.add_column('panel_panel', 'pickPosition',
                      self.gf('django.db.models.fields.FloatField')(default=316),
                      keep_default=False)

        # Adding field 'Panel.tabPosition'
        db.add_column('panel_panel', 'tabPosition',
                      self.gf('django.db.models.fields.FloatField')(default=311),
                      keep_default=False)

        # Adding field 'Panel.solderPosition'
        db.add_column('panel_panel', 'solderPosition',
                      self.gf('django.db.models.fields.FloatField')(default=443),
                      keep_default=False)

        # Adding field 'Panel.testPosition'
        db.add_column('panel_panel', 'testPosition',
                      self.gf('django.db.models.fields.FloatField')(default=527),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Panel.conveyorHeadPosition'
        db.add_column('panel_panel', 'conveyorHeadPosition',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Deleting field 'Panel.conveyorEnd'
        db.delete_column('panel_panel', 'conveyorEnd')

        # Deleting field 'Panel.pickPosition'
        db.delete_column('panel_panel', 'pickPosition')

        # Deleting field 'Panel.tabPosition'
        db.delete_column('panel_panel', 'tabPosition')

        # Deleting field 'Panel.solderPosition'
        db.delete_column('panel_panel', 'solderPosition')

        # Deleting field 'Panel.testPosition'
        db.delete_column('panel_panel', 'testPosition')


    models = {
        'panel.panel': {
            'Meta': {'object_name': 'Panel'},
            'active_area': ('django.db.models.fields.FloatField', [], {}),
            'active_margin': ('django.db.models.fields.FloatField', [], {}),
            'conveyorEnd': ('django.db.models.fields.FloatField', [], {}),
            'full_stroke': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_stroke': ('django.db.models.fields.FloatField', [], {}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'margin': ('django.db.models.fields.FloatField', [], {}),
            'panelId': ('django.db.models.fields.TextField', [], {}),
            'pickCenterToSoletteEdge': ('django.db.models.fields.FloatField', [], {}),
            'pickPosition': ('django.db.models.fields.FloatField', [], {}),
            'solderPosition': ('django.db.models.fields.FloatField', [], {}),
            'solette_length': ('django.db.models.fields.FloatField', [], {}),
            'solette_spacing': ('django.db.models.fields.FloatField', [], {}),
            'strokePosition': ('django.db.models.fields.FloatField', [], {}),
            'stroke_end': ('django.db.models.fields.FloatField', [], {}),
            'stroke_lead': ('django.db.models.fields.FloatField', [], {}),
            'tabPosition': ('django.db.models.fields.FloatField', [], {}),
            'testPosition': ('django.db.models.fields.FloatField', [], {}),
            'voltage': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['panel']