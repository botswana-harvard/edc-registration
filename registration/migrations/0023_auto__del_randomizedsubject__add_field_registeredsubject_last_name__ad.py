# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding field 'RegisteredSubject.last_name'
        db.add_column('bhp_registration_registeredsubject', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True), keep_default=False)

        # Adding field 'RegisteredSubject.identity_type'
        db.add_column('bhp_registration_registeredsubject', 'identity_type', self.gf('django.db.models.fields.CharField')(default=0, max_length=15), keep_default=False)

        # Adding field 'RegisteredSubject.salt'
        db.add_column('bhp_registration_registeredsubject', 'salt', self.gf('django.db.models.fields.CharField')(default='0W,FKWDbd(C>', max_length=25), keep_default=False)

        # Adding field 'RegisteredSubjectAudit.last_name'
        db.add_column('bhp_registration_registeredsubject_audit', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True), keep_default=False)

        # Adding field 'RegisteredSubjectAudit.identity_type'
        db.add_column('bhp_registration_registeredsubject_audit', 'identity_type', self.gf('django.db.models.fields.CharField')(default=0, max_length=15), keep_default=False)

        # Adding field 'RegisteredSubjectAudit.salt'
        db.add_column('bhp_registration_registeredsubject_audit', 'salt', self.gf('django.db.models.fields.CharField')(default='0W,FKWDbd(C>', max_length=25), keep_default=False)

    def backwards(self, orm):
        
        raise RuntimeError("Cannot reverse this migration.")

        # Adding model 'RandomizedSubject'
        db.create_table('bhp_registration_randomizedsubject', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('subject_consent_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('screening_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('randomization_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('subject_type', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('subject_identifier', self.gf('django.db.models.fields.CharField')(blank=True, max_length=36, null=True, db_index=True)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('registration_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('registration_status', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('bhp_registration', ['RandomizedSubject'])

        # Deleting field 'RegisteredSubject.last_name'
        db.delete_column('bhp_registration_registeredsubject', 'last_name')

        # Deleting field 'RegisteredSubject.identity_type'
        db.delete_column('bhp_registration_registeredsubject', 'identity_type')

        # Deleting field 'RegisteredSubject.salt'
        db.delete_column('bhp_registration_registeredsubject', 'salt')

        # User chose to not deal with backwards NULL issues for 'RegisteredSubject.first_name'
        raise RuntimeError("Cannot reverse this migration. 'RegisteredSubject.first_name' and its values cannot be restored.")

        # Changing field 'RegisteredSubject.identity'
        db.alter_column('bhp_registration_registeredsubject', 'identity', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # User chose to not deal with backwards NULL issues for 'RegisteredSubject.initials'
        raise RuntimeError("Cannot reverse this migration. 'RegisteredSubject.initials' and its values cannot be restored.")

        # Deleting field 'RegisteredSubjectAudit.last_name'
        db.delete_column('bhp_registration_registeredsubject_audit', 'last_name')

        # Deleting field 'RegisteredSubjectAudit.identity_type'
        db.delete_column('bhp_registration_registeredsubject_audit', 'identity_type')

        # Deleting field 'RegisteredSubjectAudit.salt'
        db.delete_column('bhp_registration_registeredsubject_audit', 'salt')

        # User chose to not deal with backwards NULL issues for 'RegisteredSubjectAudit.first_name'
        raise RuntimeError("Cannot reverse this migration. 'RegisteredSubjectAudit.first_name' and its values cannot be restored.")

        # Changing field 'RegisteredSubjectAudit.identity'
        db.alter_column('bhp_registration_registeredsubject_audit', 'identity', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # User chose to not deal with backwards NULL issues for 'RegisteredSubjectAudit.initials'
        raise RuntimeError("Cannot reverse this migration. 'RegisteredSubjectAudit.initials' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SubjectIdentifierAuditTrail.first_name'
        raise RuntimeError("Cannot reverse this migration. 'SubjectIdentifierAuditTrail.first_name' and its values cannot be restored.")

        # Adding field 'SubjectIdentifierAuditTrail.dob'
        db.add_column('bhp_registration_subjectidentifieraudittrail', 'dob', self.gf('django.db.models.fields.DateTimeField')(null=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'SubjectIdentifierAuditTrail.initials'
        raise RuntimeError("Cannot reverse this migration. 'SubjectIdentifierAuditTrail.initials' and its values cannot be restored.")


    models = {
        'bhp_registration.registeredsubject': {
            'Meta': {'ordering': "['subject_identifier']", 'object_name': 'RegisteredSubject'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_identifier': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'relative_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'default': "'0W,FKWDbd(C>'", 'unique': 'True', 'max_length': '25'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True', 'blank': 'True'}),
            'subject_consent_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_registration.registeredsubjectaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'RegisteredSubjectAudit', 'db_table': "'bhp_registration_registeredsubject_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_identifier': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'relative_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'default': "'0W,FKWDbd(C>'", 'max_length': '25'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_registeredsubject'", 'null': 'True', 'to': "orm['bhp_variables.StudySite']"}),
            'subject_consent_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_registration.subjectidentifieraudittrail': {
            'Meta': {'ordering': "['-date_allocated']", 'object_name': 'SubjectIdentifierAuditTrail'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_allocated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 6, 25)'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'subject_consent_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_variables.studysite': {
            'Meta': {'ordering': "['site_code']", 'unique_together': "[('site_code', 'site_name')]", 'object_name': 'StudySite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'site_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        }
    }

    complete_apps = ['bhp_registration']
