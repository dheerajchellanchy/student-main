# Generated by Django 3.2.9 on 2023-03-13 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nvt', '0004_rename_profile_leave_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='Profile',
            new_name='profile',
        ),
    ]