# Generated by Django 4.1.2 on 2022-10-31 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fasteners', '0019_alter_din7500d_options_alter_iso14583_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iso14583',
            options={'verbose_name': 'ISO 14583', 'verbose_name_plural': 'ISO 14583'},
        ),
    ]
