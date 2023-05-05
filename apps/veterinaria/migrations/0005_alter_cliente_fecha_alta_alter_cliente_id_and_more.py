# Generated by Django 4.2 on 2023-05-04 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0004_alter_cliente_fecha_alta_historiaclinica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 4, 20, 58, 51, 225800), max_length=15, verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha_consulta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 4, 20, 58, 51, 225800), max_length=15, verbose_name='Fecha de consulta'),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipomascota',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]