# edc-registration

[![Build Status](https://travis-ci.org/botswana-harvard/edc-registration.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-registration) [![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-registration/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-registration?branch=develop)

The model `RegisteredSubject` is used by the Edc as the master subject registration table. Only one record may exist per individual. This model is used by other models as a link the subject. Some models explicitly include a foreign key to `RegisteredSubject` while others will reach `RegisteredSubject`, for example, via a foreign key to a visit tracking model.

* `RegisteredSubject` is completed in a signal and not by the user. As other models that collect the required information are created the signal will update. The best model to use is the ICF. You need to write and connect the signal yourself. See `edc_consent`.
* Registration models such as eligibility model forms usually have a foreign key `RegisteredSubject`. Registration models are usually configured as "membership forms" and register a subject to one or more a pre-defined visit schedules. See `edc_visit_schedule`.
* The `Appointment` model has a foreign key to `RegisteredSubject`. See `edc_appoinment`.
* Crf models usually reach  `RegisteredSubject` via a foreign key to a visit tracking model which has a foreign key to `Appointment`. See `edc_visit_tracking` and `edc_appointment`.

In settings you need to add the types of subjects that will be registered and if there is a registration cap on any of them. Field `subject_type` is a required on the `RegisteredSubject` model.

If you are using the defaults, then there is no need to explicitly define these attributes in `settings.py`. The defaults are this:

    SUBJECT_TYPES = ['subject']
    MAX_SUBJECTS = {'subject': -1}

If you have something other than the defaults, they might look like this:

    SUBJECT_TYPES = ['mother', 'infant']
    MAX_SUBJECTS = {'mother': 3000, 'infants': -1}

If there is no registration cap for a given subject type, set the number to -1.
    
