# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('escolha', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pergunta', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'data de publicacao')),
            ],
        ),
        migrations.AddField(
            model_name='escolha',
            name='pergunta',
            field=models.ForeignKey(to='polls.Pergunta'),
        ),
    ]
