# Generated by Django 4.1.3 on 2022-11-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
