# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150808_0801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='pub_date',
        ),
    ]
