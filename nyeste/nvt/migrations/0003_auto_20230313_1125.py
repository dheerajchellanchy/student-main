# Generated by Django 3.2.9 on 2023-03-13 05:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nvt', '0002_auto_20230313_1112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emp',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='emp',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='leave',
            old_name='emp',
            new_name='Profile',
        ),
    ]
