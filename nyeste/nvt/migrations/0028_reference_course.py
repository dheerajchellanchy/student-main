# Generated by Django 4.1.7 on 2023-03-21 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nvt', '0027_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nvt.course'),
        ),
    ]
