# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]
