# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_pergunta_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 8, 11, 7, 12, 905000, tzinfo=utc), verbose_name=b'data de publicacao'),
            preserve_default=False,
        ),
    ]
