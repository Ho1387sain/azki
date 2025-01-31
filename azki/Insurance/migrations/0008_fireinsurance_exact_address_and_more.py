# Generated by Django 5.1.3 on 2024-12-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0007_rename_average_cost_fireinsurance_build_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fireinsurance',
            name='Exact_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='Expiration_date_previous_insurance',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='Landline_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='Number_of_floors',
            field=models.PositiveIntegerField(blank=True, default='1', null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='floor',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='name_family',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='national_code_Insurer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='tag',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='unit',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='zip_code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fireinsurance',
            name='Insurance_Matters',
            field=models.CharField(blank=True, choices=[('c', 'کامل (بنا و لوازم خانه)'), ('l', 'لوازم خانه'), ('b', 'بنا')], default=' ', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fireinsurance',
            name='Number_Of_Units',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='fireinsurance',
            name='Property_Type',
            field=models.CharField(blank=True, choices=[('a', 'یک واحد اپارتمان'), ('v', 'یک ساختمان ویلایی'), ('m', 'اپارتمان یا مجتمع')], default=' ', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fireinsurance',
            name='build_Type',
            field=models.CharField(blank=True, choices=[('f', 'فلزی'), ('a', 'اجری'), ('b', 'بتنی')], default=' ', max_length=10, null=True),
        ),
    ]
