# Generated by Django 5.1.3 on 2024-12-09 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_userprofile_user_userprofile_ostan_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='f_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='l_name',
        ),
    ]
