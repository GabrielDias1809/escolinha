# Generated by Django 4.1.5 on 2023-01-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_remove_aula_hora_aula_detalhes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='detalhes',
        ),
        migrations.AlterField(
            model_name='aula',
            name='data',
            field=models.DateTimeField(),
        ),
    ]