# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170414_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dreamreal',
            name='din',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dreamreal',
            name='dout',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dreamreal',
            name='dtot',
            field=models.CharField(max_length=50),
        ),
    ]