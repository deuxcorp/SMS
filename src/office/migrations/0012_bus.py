# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_subject'),
        ('office', '0011_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('bus_route', models.CharField(blank=True, max_length=255, null=True)),
                ('driver_name', models.CharField(blank=True, max_length=255, null=True)),
                ('driver_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.School')),
            ],
        ),
    ]
