# Generated by Django 5.1.3 on 2024-12-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0009_alter_fireinsurance_expiration_date_previous_insurance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
