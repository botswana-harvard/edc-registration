from edc_base.model_mixins import BaseUuidModel

from .model_mixins import RegisteredSubjectModelMixin


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_registration'
