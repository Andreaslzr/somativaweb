# Generated by Django 4.2.6 on 2023-10-12 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_automovel_clientefk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovel',
            name='clienteFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automovelCliente', to='main.cliente'),
        ),
    ]
