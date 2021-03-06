# Generated by Django 3.1.6 on 2021-03-01 15:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0009_auto_20210301_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 15, 9, 26, 769274, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 15, 9, 26, 805088, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 15, 9, 26, 805088, tzinfo=utc)),
        ),
    ]
