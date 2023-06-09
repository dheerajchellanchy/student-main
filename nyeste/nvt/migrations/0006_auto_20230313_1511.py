# Generated by Django 3.2.9 on 2023-03-13 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nvt', '0005_rename_profile_attendance_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('code', models.CharField(default='adminnotviewed', max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='accountnumber',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ifsccode',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='language',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='office',
        ),
        migrations.AddField(
            model_name='profile',
            name='reg_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Staff', 'Staff'), ('Parent', 'Parent'), ('Admin', 'Admin')], default='Student', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nvt.course'),
        ),
    ]
