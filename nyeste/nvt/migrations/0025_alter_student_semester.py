# Generated by Django 4.1.7 on 2023-03-21 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nvt', '0024_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nvt.semester'),
        ),
    ]
