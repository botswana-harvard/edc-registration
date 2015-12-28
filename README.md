# edc-registration

[![Build Status](https://travis-ci.org/botswana-harvard/edc-registration.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-registration) [![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-registration/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-registration?branch=develop)

The model `RegisteredSubject` is used by the Edc as the master subject registration table. Only one record may exist per individual. This model by other models as a link the subject. Some models explicitly include a foregin key to `RegisteredSubject` while others will reach `RegisteredSubject` via a foreign key to a visit tracking model.

* Registration models such as eligibility forms usually have a foregin key to `RegisteredSubject`.
* Crf models usually reach  `RegisteredSubject` via a foreign key to the visit tracking model.

In settings you can add the types of subjects that will be registered and if there is a registration cap. The `subject_type` is a required field on the `RegisteredSubject` model.

If you are using the defaults, then there is no need to explicitly define these attributes in `settings.py`. The defaults are this:

    SUBJECT_TYPES = ['subject']
    MAX_SUBJECTS = {'subject': -1}

If you have something other than the defaults, they might look like this:

    SUBJECT_TYPES = ['mother', 'infant']
    MAX_SUBJECTS = {'mother': 3000, 'infants': -1}

If there is no registration cap for a given subject type, set the number to -1.
    