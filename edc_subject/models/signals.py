# from django.db.models.signals import post_save
# from django.dispatch import receiver
# 
# from edc.base.model.constants import BASE_MODEL_UPDATE_FIELDS, BASE_UUID_MODEL_UPDATE_FIELDS
# 
# from .base_subject import BaseSubject
# 
# 
# @receiver(post_save, weak=False, dispatch_uid='base_subject_get_or_create_registered_subject_on_post_save')
# def base_subject_get_or_create_registered_subject_on_post_save(sender, instance, raw, created, using, update_fields, **kwargs):
#     if not raw:
#         if isinstance(instance, (BaseConsent, )):
#             try:
#                 if instance.registered_subject:
#                     instance.registered_subject = instance._update_registered_subject(using)
#                 else:
#                     instance.registered_subject = instance._get_or_created_registered_subject(using)
#             except AttributeError as attribute_error:
#                 # self does not have a foreign key to RegisteredSubject but RegisteredSubject
#                 # still needs to be created or updated
#                 instance._get_or_created_registered_subject(using)
#                 if not created:
#                     instance._update_registered_subject(using, registered_subject)
#             instance.registered_subject.save(using=using)
# #             if updated:
# #                 post_save.disconnect(base_subject_get_or_create_registered_subject_on_post_save, sender=sender)
# #                 instance.save()
# #                 post_save.connect(base_subject_get_or_create_registered_subject_on_post_save, sender=sender)
