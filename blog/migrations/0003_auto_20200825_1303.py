# Generated by Django 2.2.14 on 2020-08-25 12:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='profile',
            new_name='profile_text',
        ),
        migrations.AddField(
            model_name='cv',
            name='additionalskills_text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='additionalskills_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='education_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='education_header',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='education_text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='education_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='profile_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='workexperience_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='workexperience_header',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='workexperience_text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='workexperience_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
