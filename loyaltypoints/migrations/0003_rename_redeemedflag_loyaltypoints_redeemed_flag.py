# Generated by Django 3.2 on 2023-01-22 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyaltypoints', '0002_loyaltypoints_redeemedflag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loyaltypoints',
            old_name='redeemedFlag',
            new_name='redeemed_flag',
        ),
    ]
