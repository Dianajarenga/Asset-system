# Generated by Django 3.2.4 on 2021-08-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0004_auto_20210820_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendars',
            name='end_time',
            field=models.TimeField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='event_agenda',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='event_name',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='start_time',
            field=models.TimeField(blank=True, max_length=9, null=True),
        ),
    ]
