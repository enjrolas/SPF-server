# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FactoryState.tabberPosition'
        db.add_column('factoryState_factorystate', 'tabberPosition',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState.pickPosition'
        db.add_column('factoryState_factorystate', 'pickPosition',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState.soldererPosition'
        db.add_column('factoryState_factorystate', 'soldererPosition',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState.testPosition'
        db.add_column('factoryState_factorystate', 'testPosition',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState.endPosition'
        db.add_column('factoryState_factorystate', 'endPosition',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FactoryState.tabberPosition'
        db.delete_column('factoryState_factorystate', 'tabberPosition')

        # Deleting field 'FactoryState.pickPosition'
        db.delete_column('factoryState_factorystate', 'pickPosition')

        # Deleting field 'FactoryState.soldererPosition'
        db.delete_column('factoryState_factorystate', 'soldererPosition')

        # Deleting field 'FactoryState.testPosition'
        db.delete_column('factoryState_factorystate', 'testPosition')

        # Deleting field 'FactoryState.endPosition'
        db.delete_column('factoryState_factorystate', 'endPosition')


    models = {
        'factoryState.factorystate': {
            'Meta': {'object_name': 'FactoryState'},
            'backingLength': ('django.db.models.fields.FloatField', [], {}),
            'backingWidth': ('django.db.models.fields.FloatField', [], {}),
            'backingsInHopper': ('django.db.models.fields.IntegerField', [], {}),
            'conveyorPosition': ('django.db.models.fields.FloatField', [], {}),
            'encapsulantInTub': ('django.db.models.fields.IntegerField', [], {}),
            'endPosition': ('django.db.models.fields.FloatField', [], {}),
            'factoryId': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'halfAdvance': ('django.db.models.fields.FloatField', [], {}),
            'holeLength': ('django.db.models.fields.FloatField', [], {}),
            'holeOffset': ('django.db.models.fields.FloatField', [], {}),
            'hopperPosition': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'padLength': ('django.db.models.fields.FloatField', [], {}),
            'pickPosition': ('django.db.models.fields.FloatField', [], {}),
            'soldererPosition': ('django.db.models.fields.FloatField', [], {}),
            'soletteLength': ('django.db.models.fields.FloatField', [], {}),
            'soletteSpacing': ('django.db.models.fields.FloatField', [], {}),
            'soletteThickness': ('django.db.models.fields.FloatField', [], {}),
            'soletteWidth': ('django.db.models.fields.FloatField', [], {}),
            'solettesInHopper': ('django.db.models.fields.IntegerField', [], {}),
            'suctionDelay': ('django.db.models.fields.IntegerField', [], {}),
            'suctionReleaseTime': ('django.db.models.fields.IntegerField', [], {}),
            'tabberPosition': ('django.db.models.fields.FloatField', [], {}),
            'tabbingConnection': ('django.db.models.fields.FloatField', [], {}),
            'tabbingLength': ('django.db.models.fields.FloatField', [], {}),
            'tabbingOffset': ('django.db.models.fields.FloatField', [], {}),
            'tabbingOnSpool': ('django.db.models.fields.IntegerField', [], {}),
            'testPosition': ('django.db.models.fields.FloatField', [], {}),
            'var_1ma': ('django.db.models.fields.IntegerField', [], {}),
            'var_1pm': ('django.db.models.fields.IntegerField', [], {}),
            'var_1po': ('django.db.models.fields.IntegerField', [], {}),
            'var_1tr': ('django.db.models.fields.FloatField', [], {}),
            'var_2ma': ('django.db.models.fields.IntegerField', [], {}),
            'var_2pm': ('django.db.models.fields.IntegerField', [], {}),
            'var_2po': ('django.db.models.fields.IntegerField', [], {}),
            'var_2tr': ('django.db.models.fields.FloatField', [], {}),
            'var_3ma': ('django.db.models.fields.IntegerField', [], {}),
            'var_3pm': ('django.db.models.fields.IntegerField', [], {}),
            'var_3po': ('django.db.models.fields.IntegerField', [], {}),
            'var_3tr': ('django.db.models.fields.FloatField', [], {}),
            'var_4ma': ('django.db.models.fields.IntegerField', [], {}),
            'var_4pm': ('django.db.models.fields.IntegerField', [], {}),
            'var_4po': ('django.db.models.fields.IntegerField', [], {}),
            'var_4tr': ('django.db.models.fields.FloatField', [], {}),
            'var_afr': ('django.db.models.fields.IntegerField', [], {}),
            'var_asa': ('django.db.models.fields.FloatField', [], {}),
            'var_avm': ('django.db.models.fields.IntegerField', [], {}),
            'var_xfr': ('django.db.models.fields.IntegerField', [], {}),
            'var_xsa': ('django.db.models.fields.FloatField', [], {}),
            'var_xvm': ('django.db.models.fields.IntegerField', [], {}),
            'var_yfr': ('django.db.models.fields.IntegerField', [], {}),
            'var_ysa': ('django.db.models.fields.FloatField', [], {}),
            'var_yvm': ('django.db.models.fields.IntegerField', [], {}),
            'var_zfr': ('django.db.models.fields.IntegerField', [], {}),
            'var_zsa': ('django.db.models.fields.FloatField', [], {}),
            'var_zvm': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['factoryState']