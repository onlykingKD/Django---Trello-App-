# Generated by Django 3.1.6 on 2021-03-01 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 11, 22, 3, 897529, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 11, 22, 3, 969328, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 11, 22, 3, 969328, tzinfo=utc)),
        ),
    ]
