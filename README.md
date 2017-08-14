# edc-registration

[![Build Status](https://travis-ci.org/botswana-harvard/edc-registration.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-registration) [![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-registration/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-registration?branch=develop)

The model `RegisteredSubject` is used by the Edc as the master subject registration table. Only one record may exist per individual. The table has space for PII so typically a `RegisteredSubject` instance is created or updated on completion of the informed consent. As always, PII in the Edc is encrypted at rest using `django-crypto-field`.

### RegisteredSubjectModelMixin
Declare `RegisteredSubject` in your app using the `RegisteredSubjectModelMixin`, for example:

    class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):
        class Meta:
            app_label = 'my_app'
            
then in `edc_registration` AppConfig specify the `app_label = 'my_app'` so that other modules in the Edc can find the model class. (Note: The model_name is assumed to always be `RegisteredSubject`). 

Other modules can find the model class by accessing the AppConfig:

    >>> from django.apps import apps as django_apps
    >>> RegisteredSubject = django_apps.get_app_config('edc_registration').model
    >>> RegisteredSubject.objects.get(subject_identifier='12345678-9')
    <RegisteredSubject: 12345678-9>

### UpdatesOrCreatesRegistrationModelMixin

`RegisteredSubject` is never edited directly by the user. Instead some other model with the needed attributes is used as a proxy. To have a model perform the task of creating or updating  `RegisteredSubject`, declare it with the `UpdatesOrCreatesRegistrationModelMixin`.

For example, a model, `SubjectEligibility` or a screening model creates or updates a `RegisteredSubject` without a subject identifier then a model such as the `SubjectConsent` in `tests.models`, also creates or updates a subject's `RegisteredSubject` instance on save. For this to happen, both models are declared with the `UpdatesOrCreatesRegistrationModelMixin`:

	class SubjectEligibility(UniqueSubjectIdentifierModelMixin, UpdatesOrCreatesRegistrationModelMixin, BaseUuidModel):

    screening_identifier = models.CharField(
        max_length=36,
        null=True,
        unique=True)

	@property
    def registration_unique_field(self):
        return 'screening_identifier'

    def update_subject_identifier_on_save(self):
        """Overridden to not set the subject identifier on save.
        """
        if not self.subject_identifier:
            self.subject_identifier = self.subject_identifier_as_pk.hex
            self.subject_identifier_aka = self.subject_identifier_as_pk.hex
        return self.subject_identifier

    class SubjectConsent(ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin, CreateAppointmentsMixin,
                         IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
                         CitizenFieldsMixin, VulnerabilityFieldsMixin, BaseUuidModel):
                         
		@property
	    def registration_unique_field(self):
	        return 'screening_identifier'

	    class Meta:
	        app_label = 'my_app'
    

The property `registration_unique_field` returns a model attribute that is used to set a registration identifier on `RegisteredSubject`.

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

Since the `app_label` of the model class `RegisteredSubject` is not known when the models classes are loaded, it is difficult to include the class as a foreign key. As a work around, use the `RegisteredSubjectMixin`. When this mixin is declared on your model, the `subject_identifier` field is added to the model and verified against `RegisteredSubject` on each save.

The `subject_identifier` field is added with `editable=False`. You must provide the correct subject identifier programmatically or the model will raise an `RegisteredSubject.DoesNotExist` exception on save.


     