# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0007_directorio_modificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorio',
            name='eliminado',
            field=models.CharField(default='1', max_length=1, null=True),
        ),
    ]