# Generated by Django 5.1.1 on 2024-10-09 00:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], default='FIAT', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serialCarroceria', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('serialMotor', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('categoria', models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='PARTICULAR', max_length=20)),
                ('precio', models.FloatField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'vehiculo',
                'verbose_name_plural': 'vehiculos',
                'ordering': ['-creado'],
                'permissions': (('es_miembro_1', 'Es miembro con prioridad 1'),),
            },
        ),
    ]
