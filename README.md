# edc-registration


In settings add the types of subjects that will be registered and if there is a registration cap. If there is no registration cap for a given subject type, set the number to -1.

    SUBJECT_TYPES = ['mother', 'infant']  # default is ['subject']
    MAX_SUBJECTS = {'mother': 1000, 'infants': -1}  # if subject_types == ['subject'], defaults to {'subject': -1}
