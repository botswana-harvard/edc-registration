# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SubjectConfiguration'
        db.delete_table('bhp_subject_subjectconfiguration')


    def backwards(self, orm):
        # Adding model 'SubjectConfiguration'
        db.create_table('bhp_subject_subjectconfiguration', (
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('default_appt_type', self.gf('django.db.models.fields.CharField')(default='clinic', max_length=10)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
        ))
        db.send_create_signal('bhp_subject', ['SubjectConfiguration'])


    models = {
        
    }

    complete_apps = ['bhp_subject']