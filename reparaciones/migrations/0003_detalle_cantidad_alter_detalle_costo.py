# Generated by Django 4.0.3 on 2022-04-19 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparaciones', '0002_alter_detalle_reparacion_alter_detalle_servicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='costo',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
    ]