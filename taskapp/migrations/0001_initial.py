# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField(null=True)),
                ('director', models.CharField(blank=True, max_length=25, null=True)),
                ('genre', models.CharField(max_length=25, null=True)),
                ('imdb_score', models.FloatField(null=True)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
