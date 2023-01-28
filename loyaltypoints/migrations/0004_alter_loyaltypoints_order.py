# Generated by Django 3.2 on 2023-01-22 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
        ('loyaltypoints', '0003_rename_redeemedflag_loyaltypoints_redeemed_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loyaltypoints',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loyaltypoints', to='checkout.order'),
        ),
    ]
