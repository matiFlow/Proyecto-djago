# Generated by Django 3.2 on 2022-11-12 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='marca del producto')),
            ],
            options={
                'verbose_name': 'MODELNAME',
                'verbose_name_plural': 'MODELNAMEs',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_actual', models.PositiveIntegerField(verbose_name='Existencias disponibles del producto')),
                ('stock_minimo', models.PositiveIntegerField(verbose_name='Existencias minimas del producto')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=50, verbose_name='Tipo de producto')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(max_length=50, verbose_name='precio de los productos')),
                ('existencias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.stock')),
                ('marcas', models.ManyToManyField(to='Producto.Marca')),
                ('proveedores', models.ManyToManyField(to='proveedor.Proveedor')),
                ('tipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.tipo')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
