# Generated by Django 5.1.1 on 2024-10-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0005_alter_boardsmodel_marca_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardsmodel',
            options={'ordering': ['-creado'], 'permissions': (('visualizar_catalogo', 'Can view vehiculo'), ('add_vehiculomodel', 'Can view vehiculo')), 'verbose_name': 'vehiculo', 'verbose_name_plural': 'vehiculos'},
        ),
        migrations.AlterField(
            model_name='boardsmodel',
            name='marca',
            field=models.CharField(choices=[('Ford', 'Ford'), ('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Toyota', 'Toyota')], default='FORD', max_length=20),
        ),
    ]
