from edc_base.modeladmin_mixins import ModelAdminBasicMixin


class RegisteredSubjectModelAdminMixin(ModelAdminBasicMixin):

    date_hierarchy = 'registration_datetime'

    mixin_list_display = (
        'subject_identifier',
        'dashboard',
        'first_name',
        'initials',
        'gender',
        'age',
        'subject_type',
        'sid',
        'registration_status',
        'study_site',
        'user_created',
        'created',
    )

    mixin_readonly_fields = (
        'subject_identifier',
        'subject_identifier_as_pk',
    )

    mixin_search_fields = ('subject_identifier', 'first_name', 'initials',
                           'sid', 'identity', 'id', 'registration_identifier')

    mixin_list_filter = ('subject_type', 'registration_status', 'screening_datetime',
                         'registration_datetime', 'gender',
                         'study_site', 'hiv_status', 'survival_status',
                         'may_store_samples', 'hostname_created')
