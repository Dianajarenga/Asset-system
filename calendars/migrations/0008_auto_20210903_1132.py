# Generated by Django 3.2.4 on 2021-09-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0007_calendars_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendars',
            name='end_time',
            field=models.DateTimeField(default='2021-06-08 00:00'),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='start_time',
            field=models.DateTimeField(default='2021-06-08 00:00'),
        ),
    ]
