# Generated by Django 5.1.6 on 2025-03-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(related_name='following', through='profiles.Follow', to='profiles.userprofile'),
        ),
    ]
