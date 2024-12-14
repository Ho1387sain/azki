# Generated by Django 5.1.3 on 2024-12-09 06:35

import django.db.models.deletion
import iranian_cities.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_userprofile_national_code_and_more'),
        ('iranian_cities', '0004_remove_abadi_shhahr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Ostan',
            field=iranian_cities.fields.OstanField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iranian_cities.ostan'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Shahr',
            field=iranian_cities.fields.ShahrestanField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iranian_cities.shahrestan'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='f_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='l_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='national_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]