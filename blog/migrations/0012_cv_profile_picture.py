# Generated by Django 2.2.14 on 2020-08-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200825_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='profile_picture',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]