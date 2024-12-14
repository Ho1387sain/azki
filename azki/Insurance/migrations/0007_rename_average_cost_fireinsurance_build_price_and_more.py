# Generated by Django 5.1.3 on 2024-12-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0006_insurancecompany_fireinsurance_average_cost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fireinsurance',
            old_name='Average_Cost',
            new_name='build_Price',
        ),
        migrations.RemoveField(
            model_name='fireinsurance',
            name='Life_Of_Structures',
        ),
        migrations.RemoveField(
            model_name='fireinsurance',
            name='Type_Of_Structures',
        ),
        migrations.RemoveField(
            model_name='fireinsurance',
            name='insurance_type',
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='build_Age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='build_Type',
            field=models.CharField(blank=True, choices=[('fire', 'فلزی'), ('mobile', 'اجری'), ('health', 'بتنی')], default=' ', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='thing_Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fireinsurance',
            name='Insurance_Matters',
            field=models.CharField(blank=True, choices=[('fire', 'کامل (بنا و لوازم خانه)'), ('mobile', 'لوازم خانه'), ('health', 'بنا')], default=' ', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fireinsurance',
            name='Property_Type',
            field=models.CharField(blank=True, choices=[('fire', 'یک واحد اپارتمان'), ('mobile', 'یک ساختمان ویلایی'), ('health', 'اپارتمان یا مجتمع')], default=' ', max_length=10, null=True),
        ),
    ]