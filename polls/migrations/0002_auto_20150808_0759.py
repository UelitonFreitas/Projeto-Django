# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='pub_date',
            field=models.DateField(verbose_name=b'data de publicacao'),
        ),
    ]
