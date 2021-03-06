# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170924_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='down',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='踩'),
        ),
        migrations.AlterField(
            model_name='article',
            name='up',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='赞'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='头像'),
        ),
    ]
