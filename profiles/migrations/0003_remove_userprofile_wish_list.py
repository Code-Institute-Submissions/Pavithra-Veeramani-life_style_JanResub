# Generated by Django 3.2 on 2022-12-15 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_wish_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='wish_list',
        ),
    ]
