# Generated by Django 4.1.2 on 2022-10-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]