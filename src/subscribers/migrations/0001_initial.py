# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-04 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scraping', '0010_auto_20190102_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='e-mail')),
                ('password', models.CharField(max_length=25, verbose_name='Password')),
                ('is_active', models.BooleanField(default=True, verbose_name='Status')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='City')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Specialty', verbose_name='Specialty')),
            ],
            options={
                'verbose_name_plural': 'Subscribers',
            },
        ),
    ]
