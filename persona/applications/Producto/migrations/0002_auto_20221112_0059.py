# Generated by Django 3.2 on 2022-11-12 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marca',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='tipos',
            new_name='tipo',
        ),
    ]