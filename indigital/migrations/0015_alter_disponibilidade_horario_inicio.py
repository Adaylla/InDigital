# Generated by Django 5.1.6 on 2025-02-19 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indigital', '0014_rename_horario_disponibilidade_horario_fim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidade',
            name='horario_inicio',
            field=models.TimeField(),
        ),
    ]
