# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-30 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acuse',
            name='obsequio',
        ),
        migrations.AddField(
            model_name='acuse',
            name='alias',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='directorio',
            name='acuse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='directorio.Acuse'),
        ),
    ]
