# Generated by Django 4.1.2 on 2022-10-31 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasteners', '0017_alter_iso14583_options_alter_iso14583_st2_9_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DIN7500D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screw_length', models.CharField(max_length=7, unique=True)),
                ('m8', models.CharField(default='-', max_length=7, verbose_name='M8')),
                ('m10', models.CharField(default='-', max_length=7, verbose_name='M10')),
                ('m12', models.CharField(default='-', max_length=7, verbose_name='M12')),
            ],
            options={
                'verbose_name': ' DIN7500D',
                'verbose_name_plural': ' DIN7500D',
            },
        ),
    ]
