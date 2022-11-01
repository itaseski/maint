# Generated by Django 4.1.2 on 2022-10-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasteners', '0016_iso14583'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iso14583',
            options={'verbose_name': 'ISO 14583', 'verbose_name_plural': 'ISO 14583'},
        ),
        migrations.AlterField(
            model_name='iso14583',
            name='st2_9',
            field=models.CharField(default='-', max_length=7, verbose_name='ST2.9'),
        ),
        migrations.AlterField(
            model_name='iso14583',
            name='st3_5',
            field=models.CharField(default='-', max_length=7, verbose_name='ST3.5'),
        ),
        migrations.AlterField(
            model_name='iso14583',
            name='st4_2',
            field=models.CharField(default='-', max_length=7, verbose_name='ST4.2'),
        ),
        migrations.AlterField(
            model_name='iso14583',
            name='st4_8',
            field=models.CharField(default='-', max_length=7, verbose_name='ST4.8'),
        ),
        migrations.AlterField(
            model_name='iso14583',
            name='st5_5',
            field=models.CharField(default='-', max_length=7, verbose_name='ST5.5'),
        ),
        migrations.AlterField(
            model_name='iso14583',
            name='st6_3',
            field=models.CharField(default='-', max_length=7, verbose_name='ST6.3'),
        ),
    ]