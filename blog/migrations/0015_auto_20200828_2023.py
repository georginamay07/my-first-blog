# Generated by Django 2.2.14 on 2020-08-28 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='work_experience_date',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='work_experience_description',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='work_experience_location',
        ),
    ]
