# Generated by Django 4.1.5 on 2023-01-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_aula_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='data',
            field=models.DateField(),
        ),
    ]