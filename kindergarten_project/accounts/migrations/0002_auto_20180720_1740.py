# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='child',
            field=models.ManyToManyField(blank=True, related_name='childs_parent', to='groups.Child'),
        ),
    ]
