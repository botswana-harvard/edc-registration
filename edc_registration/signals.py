# from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, weak=False, dispatch_uid="update_registered_subject_from_model_on_post_save")
def update_registered_subject_from_model_on_post_save(sender, instance, raw, created, using, **kwargs):
    """Updates RegisteredSubject from models using UpdatesOrCreatesRegistrationModelMixin."""
    if not raw and not kwargs.get('update_fields'):
        try:
            instance.registration_update_or_create()
        except AttributeError as e:
            if 'registration_update_or_create' not in str(e):
                raise AttributeError(str(e))
