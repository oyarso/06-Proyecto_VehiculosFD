# Generated by Django 5.1.1 on 2024-10-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_boardsmodel_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardsmodel',
            name='marca',
            field=models.CharField(choices=[('Ford', 'Ford'), ('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Toyota', 'Toyota')], default='FORD', max_length=20),
        ),
    ]
