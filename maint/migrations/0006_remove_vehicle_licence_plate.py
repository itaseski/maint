# Generated by Django 4.1.2 on 2022-10-27 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maint', '0005_vehicle_licence_plate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='licence_plate',
        ),
    ]