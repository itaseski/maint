# Generated by Django 4.1.2 on 2022-10-26 22:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('maint', '0004_vehicle_entry_into_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='licence_plate',
            field=models.CharField(default=django.utils.timezone.now, max_length=8, unique=True),
            preserve_default=False,
        ),
    ]