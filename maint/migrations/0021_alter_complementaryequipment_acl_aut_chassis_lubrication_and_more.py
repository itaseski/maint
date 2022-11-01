# Generated by Django 4.1.2 on 2022-10-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maint', '0020_complementaryequipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complementaryequipment',
            name='acl_aut_chassis_lubrication',
            field=models.CharField(default='Without', max_length=24, verbose_name='ACL, automatic chassis lubrication'),
        ),
        migrations.AlterField(
            model_name='complementaryequipment',
            name='dimension_ja_bep_lo2o',
            field=models.CharField(default='775', max_length=24, verbose_name='Dimesion JA/BEP L020'),
        ),
        migrations.AlterField(
            model_name='complementaryequipment',
            name='spare_wheel_carrier',
            field=models.CharField(default='Without', max_length=24),
        ),
        migrations.AlterField(
            model_name='complementaryequipment',
            name='trailer_connector_type',
            field=models.CharField(default='High', max_length=24),
        ),
    ]
