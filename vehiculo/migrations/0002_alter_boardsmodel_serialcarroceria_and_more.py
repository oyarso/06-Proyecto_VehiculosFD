# Generated by Django 5.1.1 on 2024-10-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardsmodel',
            name='serialCarroceria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='boardsmodel',
            name='serialMotor',
            field=models.CharField(max_length=50),
        ),
    ]
