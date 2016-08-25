from django.core.validators import RegexValidator
from django.db import models
from django_crypto_fields.fields.encrypted_char_field import EncryptedCharField
from django_crypto_fields.fields.firstname_field import FirstnameField
from django_crypto_fields.fields.lastname_field import LastnameField

from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_registration.model_mixins import RegisteredSubjectModelMixin, RegistrationMixin


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_example'


class Enroll(RegistrationMixin, BaseUuidModel):

    identity = models.CharField(
        max_length=25)

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50,
        unique=True,
    )
    first_name = FirstnameField(
        null=True,
    )

    last_name = LastnameField(
        verbose_name="Last name",
        null=True,
    )

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.')), ],
        null=True,
    )

    dob = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=False,
        help_text="Format is YYYY-MM-DD",
    )

    class Meta:
        app_label = 'edc_example'
