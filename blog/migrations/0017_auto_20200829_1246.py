# Generated by Django 2.2.14 on 2020-08-29 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200828_2041'),
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
