# Generated by Django 4.1.2 on 2022-10-29 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fasteners', '0004_alter_size_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='DIN931',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_length', models.IntegerField()),
                ('material', models.DecimalField(decimal_places=1, default='8.8', max_digits=2)),
                ('finish', models.CharField(default='Plain Steel', max_length=24)),
            ],
            options={
                'verbose_name': 'Partly Thread DIN 933',
                'verbose_name_plural': 'DIN 931 Partly Thread',
                'ordering': ['thread_length'],
            },
        ),
        migrations.CreateModel(
            name='Size931',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default='M', max_length=6)),
                ('code', models.CharField(max_length=12, unique=True)),
                ('din931', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fasteners.din931')),
            ],
            options={
                'verbose_name': 'DIN 931 Size',
                'verbose_name_plural': 'DIN 931 Size',
            },
        ),
    ]