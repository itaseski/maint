# Generated by Django 4.1.2 on 2022-10-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasteners', '0007_screws_alter_din931_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='screws',
            options={'verbose_name': 'Screw', 'verbose_name_plural': 'Screws'},
        ),
        migrations.AlterField(
            model_name='screws',
            name='name',
            field=models.CharField(max_length=96),
        ),
    ]
