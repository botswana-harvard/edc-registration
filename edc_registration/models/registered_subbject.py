from edc_base.model.models.base_uuid_model import BaseUuidModel
from .registered_subject_model_mixin import RegisteredSubjectModelMixin


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_registration'
