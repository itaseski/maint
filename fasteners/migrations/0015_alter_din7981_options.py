# Generated by Django 4.1.2 on 2022-10-30 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fasteners', '0014_alter_din7981_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='din7981',
            options={'ordering': ['screw_length'], 'verbose_name': 'DIN 7981C', 'verbose_name_plural': 'DIN 7981C'},
        ),
    ]