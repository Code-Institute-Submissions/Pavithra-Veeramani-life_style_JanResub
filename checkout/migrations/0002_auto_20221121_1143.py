# Generated by Django 3.2 on 2022-11-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='town_or_city',
        ),
        migrations.AddField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
