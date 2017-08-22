from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.test.utils import tag
from edc_base.utils import get_utcnow

from ..models import RegisteredSubject
from .models import SubjectModelOne, SubjectModelTwo


class TestRegistration(TestCase):

    @tag('1')
    def test_creates_registered_subject(self):
        obj = SubjectModelOne.objects.create(
            screening_identifier='12345')
        try:
            RegisteredSubject.objects.get(
                registration_identifier=obj.registration_identifier)
        except ObjectDoesNotExist:
            self.fail('RegisteredSubject was unexpectedly not created')

    @tag('1')
    def test_updates_registered_subject(self):
        SubjectModelOne.objects.create(
            screening_identifier='12345',
            dob=get_utcnow() - relativedelta(years=5))

        new_dob = get_utcnow().date()
        obj = SubjectModelOne.objects.get(screening_identifier='12345')
        obj.dob = new_dob
        obj.save()

        rs = RegisteredSubject.objects.get(
            registration_identifier=obj.registration_identifier)
        self.assertEqual(rs.dob, new_dob)

    @tag('1')
    def test_creates_registered_subject_overridden(self):
        """Assert creates RegisteredSubject with registration_unique_field overridden.
        """
        obj = SubjectModelTwo.objects.create(subject_identifier='12345')
        try:
            RegisteredSubject.objects.get(
                subject_identifier=obj.subject_identifier)
        except ObjectDoesNotExist:
            self.fail('RegisteredSubject was unexpectedly not created')

    @tag('1')
    def test_updates_registered_subject_overridden(self):
        """Assert updates RegisteredSubject with registration_unique_field overridden.
        """
        SubjectModelTwo.objects.create(
            subject_identifier='12345',
            dob=get_utcnow() - relativedelta(years=5))

        new_dob = get_utcnow().date()
        obj = SubjectModelTwo.objects.get(subject_identifier='12345')
        obj.dob = new_dob
        obj.save()

        rs = RegisteredSubject.objects.get(
            subject_identifier=obj.subject_identifier)
        self.assertEqual(rs.dob, new_dob)

    @tag('4')
    def test_updates_registered_by_modeltwo(self):
        """Assert 1 model creates RegisteredSubject and the other updates it.
        """
        obj = SubjectModelOne.objects.create(
            screening_identifier='12345')
        try:
            RegisteredSubject.objects.get(
                registration_identifier=obj.registration_identifier)
        except ObjectDoesNotExist:
            self.fail('RegisteredSubject was unexpectedly not created')

        SubjectModelTwo.objects.create(
            subject_identifier='12345',
            dob=get_utcnow() - relativedelta(years=5))

        rs = RegisteredSubject.objects.all()
        self.assertEqual(rs.count(), 1)
