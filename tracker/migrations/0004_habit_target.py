# Generated by Django 4.0.6 on 2022-07-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_remove_dailyrecord_note_time_dailyrecord_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='target',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]