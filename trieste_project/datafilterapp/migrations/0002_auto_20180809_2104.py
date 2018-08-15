# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datafilterapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='long_url',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
