# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_url', models.CharField(max_length=1000, null=True)),
                ('request_type', models.CharField(max_length=1000, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('user', models.CharField(max_length=1000, null=True)),
                ('long_url', models.CharField(max_length=1000, null=True)),
                ('menu_number', models.IntegerField(null=True)),
                ('menu_type', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
