# Generated by Django 3.2 on 2022-11-12 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='cuit',
            field=models.IntegerField(verbose_name='Cuit del proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono del proveedor'),
        ),
    ]
