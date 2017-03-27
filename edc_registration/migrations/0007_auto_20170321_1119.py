# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('edc_registration', '0006_auto_20170209_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredsubject',
            name='subject_identifier_as_pk',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
