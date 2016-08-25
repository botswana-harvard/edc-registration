# edc-registration

[![Build Status](https://travis-ci.org/botswana-harvard/edc-registration.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-registration) [![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-registration/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-registration?branch=develop)

The model `RegisteredSubject` is used by the Edc as the master subject registration table. Only one record may exist per individual. The table has space for PII so typically a `RegisteredSubject` instance is created on completion of the informed consent. As always, PII in the Edc is encrypted at rest using `django-crypto-field`.

### RegisteredSubjectModelMixin
Declare `RegisteredSubject` in your app using the `RegisteredSubjectModelMixin`, for example:

    class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):
        class Meta:
            app_label = 'my_app'
            
then in `edc_registration` AppConfig specify the `app_label`, `app_label = 'my_app'` so that other modules in the Edc can find `RegisteredSubject`. (Note: The model_name is assumed to always be 'RegisteredSubject'. 

### RegistrationMixin

`RegisteredSubject` is never edited directly by the user. Instead some other model with the needed attributes is used as a proxy. To have a model perform the task of creating or updating  `RegisteredSubject`, declare it with the `RegistrationMixin`.

A model, such as the `SubjectConsent` in `edc-example` app, creates or updates a subject's `RegisteredSubject` instance on save. For this to happen, `SubjectConsent` is declared with the `RegistrationMixin`, for example:

    class SubjectConsent(ConsentModelMixin, RegistrationMixin, CreateAppointmentsMixin,
                         IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
                         CitizenFieldsMixin, VulnerabilityFieldsMixin, BaseUuidModel):

    class Meta:
        app_label = 'my_app'
    

A subject's `RegisteredSubject` instance is created and updated in a `post_save` signal. As mentioned, it is never edited directly by the user.

For the signal to be registered you need to add the AppConfig to your INSTALLED_APPS:

    INSTALLED_APPS = (
        ....
        'edc_registration.apps.AppConfig',
        ....
        )
        
However, since `RegisteredSubject` is not a model in `edc_registration`, you should subclass `AppConfig` instead, for example:

    from django.apps import AppConfig as DjangoAppConfig
    from edc_registration.apps import AppConfig as EdcRegistrationAppConfigParent
    
    class AppConfig(DjangoAppConfig):
        name = 'my_app'

    class EdcRegistrationAppConfig(EdcRegistrationAppConfigParent):
        app_label = 'my_app'

and update settings accordingly:

    INSTALLED_APPS = (
        ....
        'my_app.apps.EdcRegistrationAppConfig',
        'my_app.apps.AppConfig',
        ....
        )

### RegisteredSubjectMixin

Since the location of `app_label` of the model class `RegisteredSubject` is not known when the models classes are loaded, it is difficult to include the class as a foreign key. As a work around, use the `RegisteredSubjectMixin`. When this mixin is declared on your model, the `subject_identifier` field is added to the model and verified against `RegisteredSubject` on save.

The `subject_identifier` field is added with `editable=False`. You must provide the correct subject identifier programmatically or the model will raise an `RegisteredSubject.DoesNotExist` exception on save.


     