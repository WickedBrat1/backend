# Generated by Django 2.0.7 on 2018-10-08 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0015_auto_20181008_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 13, 19, 49, 820278)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 13, 19, 49, 819555)),
        ),
    ]
