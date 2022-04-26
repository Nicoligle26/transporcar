# Generated by Django 4.0.3 on 2022-04-18 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
        ('vehiculos', '0003_remove_infraccion_conductores_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='usuario_id',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.user'),
        ),
        migrations.AlterField(
            model_name='infraccion',
            name='conductor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.conductor'),
        ),
        migrations.AlterField(
            model_name='infraccion',
            name='vehiculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='conductor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.conductor'),
        ),
    ]
