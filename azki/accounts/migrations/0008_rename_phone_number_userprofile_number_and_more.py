# Generated by Django 5.1.3 on 2024-12-09 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
