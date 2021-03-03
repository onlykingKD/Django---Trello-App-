# Generated by Django 3.1.6 on 2021-03-01 14:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0003_auto_20210301_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 14, 41, 4, 669254, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 14, 41, 4, 949945, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello_app.tasklist'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 14, 41, 4, 949945, tzinfo=utc)),
        ),
    ]