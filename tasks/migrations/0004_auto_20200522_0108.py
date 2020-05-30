# Generated by Django 3.0.3 on 2020-05-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_userprofilemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
