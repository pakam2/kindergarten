# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=255)),
                ('type_of_group', models.CharField(choices=[('Y', 'Younger'), ('O', 'Older')], max_length=1)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Child')),
            ],
        ),
    ]