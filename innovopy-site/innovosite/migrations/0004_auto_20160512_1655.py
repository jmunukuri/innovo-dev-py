# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innovosite', '0003_auto_20160512_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='documents',
            field=models.ManyToManyField(blank=True, related_name='building_documents', to='core.DocumentFile'),
        ),
    ]
