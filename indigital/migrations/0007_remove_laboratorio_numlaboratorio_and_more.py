# Generated by Django 5.1.6 on 2025-02-14 18:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indigital', '0006_reserva_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorio',
            name='numLaboratorio',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='data',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='laboratorio',
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='num_laboratorio',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='vagas',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('data', models.DateField()),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indigital.laboratorio')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='disponibilidade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='indigital.disponibilidade'),
        ),
    ]
