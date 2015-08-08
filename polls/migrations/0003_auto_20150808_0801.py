# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150808_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'data de publicacao'),
        ),
    ]
