# Generated by Django 3.2.4 on 2021-09-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0005_auto_20210820_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendars',
            name='end_time',
            field=models.DateTimeField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendars',
            name='start_time',
            field=models.DateTimeField(default=''),
            preserve_default=False,
        ),
    ]