# Generated by Django 4.2.6 on 2023-10-05 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_mantencao_categoria_manutencao_categoria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clientes',
            new_name='cliente',
        ),
        migrations.RenameModel(
            old_name='funcionarios',
            new_name='funcionario',
        ),
    ]
