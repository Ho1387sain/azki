# Generated by Django 5.1.3 on 2024-12-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0005_mobileinsurance_city_mobileinsurance_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='Average_Cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='Insurance_Matters',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fireinsurance',
            name='insurance_type',
            field=models.CharField(choices=[('fire', 'فلزی'), ('mobile', 'اجری'), ('health', 'بتنی')], default='fire', max_length=10),
        ),
        migrations.AlterField(
            model_name='fireinsurance',
            name='Life_Of_Structures',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='fireinsurance',
            name='Type_Of_Structures',
            field=models.CharField(choices=[('fire', 'فلزی'), ('mobile', 'اجری'), ('health', 'بتنی')], default=' ', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobileinsurance',
            name='City',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='mobileinsurance',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]