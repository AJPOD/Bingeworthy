# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bingeworthy', '0004_auto_20190319_0029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAccount',
            new_name='UserPicture',
        ),
    ]
