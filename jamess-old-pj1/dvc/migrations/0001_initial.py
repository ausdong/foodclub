# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fighter'
        db.create_table('dvc_fighter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('dvc', ['Fighter'])

        # Adding model 'Warcategory'
        db.create_table('dvc_warcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('challenger', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dvc.Fighter'], related_name='challenger')),
            ('challenged', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dvc.Fighter'], related_name='challenged')),
        ))
        db.send_create_signal('dvc', ['Warcategory'])

        # Adding model 'Prompt'
        db.create_table('dvc_prompt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dvc.Warcategory'])),
            ('prompt_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('dvc', ['Prompt'])

        # Adding model 'Battle'
        db.create_table('dvc_battle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prompt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dvc.Prompt'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dvc.Fighter'], related_name='winner')),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('dvc', ['Battle'])

        # Adding model 'Face'
        db.create_table('dvc_face', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fighter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dvc.Fighter'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('dvc', ['Face'])


    def backwards(self, orm):
        # Deleting model 'Fighter'
        db.delete_table('dvc_fighter')

        # Deleting model 'Warcategory'
        db.delete_table('dvc_warcategory')

        # Deleting model 'Prompt'
        db.delete_table('dvc_prompt')

        # Deleting model 'Battle'
        db.delete_table('dvc_battle')

        # Deleting model 'Face'
        db.delete_table('dvc_face')


    models = {
        'dvc.battle': {
            'Meta': {'object_name': 'Battle'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prompt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dvc.Prompt']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dvc.Fighter']", 'related_name': "'winner'"})
        },
        'dvc.face': {
            'Meta': {'object_name': 'Face'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'fighter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dvc.Fighter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dvc.fighter': {
            'Meta': {'object_name': 'Fighter'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dvc.prompt': {
            'Meta': {'object_name': 'Prompt'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dvc.Warcategory']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prompt_text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dvc.warcategory': {
            'Meta': {'object_name': 'Warcategory'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'challenged': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dvc.Fighter']", 'related_name': "'challenged'"}),
            'challenger': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dvc.Fighter']", 'related_name': "'challenger'"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['dvc']