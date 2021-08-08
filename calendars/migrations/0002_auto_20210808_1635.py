# Generated by Django 3.2.4 on 2021-08-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendars',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='calendars',
            name='price',
        ),
        migrations.RemoveField(
            model_name='calendars',
            name='type',
        ),
        migrations.AddField(
            model_name='calendars',
            name='event_agenda',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='calendars',
            name='event_attendees',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calendars',
            name='event_duration',
            field=models.TimeField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='calendars',
            name='event_name',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='calendars',
            name='event_organizer',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='calendars',
            name='event_venue',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
    ]
