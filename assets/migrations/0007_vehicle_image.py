# Generated by Django 4.1.3 on 2022-11-04 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_remove_vehicle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
