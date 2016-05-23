# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-17 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20160517_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelink',
            name='notification',
            field=models.ManyToManyField(blank=True, to='web.NotificationLinks'),
        ),
        migrations.AlterField(
            model_name='newgraduates',
            name='img',
            field=models.ImageField(help_text='\u786e\u4fdd\u56fe\u7247\u88c1\u526a\u81f3650x397,\u4e14\u5206\u8fa8\u7387\u4e3a300', upload_to=b'static/img/home//', verbose_name='\u9875\u9762\u663e\u793a\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='publicclass',
            name='img',
            field=models.ImageField(help_text='\u786e\u4fdd\u56fe\u7247\u88c1\u526a\u81f3650x397,\u4e14\u5206\u8fa8\u7387\u4e3a300', upload_to=b'static/img/home/public_class/', verbose_name='\u9875\u9762\u663e\u793a\u56fe\u7247'),
        ),
    ]
