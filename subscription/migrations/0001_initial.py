# Generated by Django 3.2 on 2023-01-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
