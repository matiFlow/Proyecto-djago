# Generated by Django 3.2 on 2022-11-12 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del proveedor')),
                ('cuit', models.IntegerField(max_length=50, verbose_name='Cuit del proveedor')),
                ('telefono', models.IntegerField(max_length=20, verbose_name='Telefono del proveedor')),
            ],
            options={
                'verbose_name': 'Provedor',
                'verbose_name_plural': 'Provedoors',
            },
        ),
    ]
