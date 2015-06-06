# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_signup_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 5, 21, 48, 26, 833714, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 5, 21, 48, 43, 351531, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
