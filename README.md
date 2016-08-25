# edc-registration

[![Build Status](https://travis-ci.org/botswana-harvard/edc-registration.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-registration) [![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-registration/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-registration?branch=develop)

The model `RegisteredSubject` is used by the Edc as the master subject registration table. Only one record may exist per individual. The table has space for PII so typically a `RegisteredSubject` instance is created on completion of the informed consent. As always, PII in the Edc is encrypted at rest using `django-crypto-field`.

A model, such as the `SubjectConsent` in `edc-example` app, creates or updates a subject's `RegisteredSubject` instance on save. For this to happen, `SubjectConsent` is declared with the `RegistrationMixin`, for example:

    class SubjectConsent(ConsentModelMixin, RegistrationMixin, CreateAppointmentsMixin,
                         IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
                         CitizenFieldsMixin, VulnerabilityFieldsMixin, BaseUuidModel):

    class Meta:
        app_label = 'my_app'
    

A subject's `RegisteredSubject` instance is created and updated in a `post_save` signal. It is never edited directly by the user.

For the signal to be registered you need to add the AppConfig to your INSTALLED_APPS:

    INSTALLED_APPS = (
        ....
        'edc_registration.apps.AppConfig',
        ....
        )
        
However, since `RegisteredSubject` is not a model in `edc_registration`, you should subclass `AppConfig`, for example:

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
