# Generated by Django 4.1.2 on 2022-10-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maint', '0024_alter_complementaryequipment_bracket_front_mounted_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complementaryequipment',
            name='acl_aut_chassis_lubrication',
            field=models.CharField(default='Нема', max_length=24, verbose_name='ACL, automatic chassis lubrication'),
        ),
    ]
