# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_location_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='hours',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 7, 19, 21, 24, 5, 996019, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
