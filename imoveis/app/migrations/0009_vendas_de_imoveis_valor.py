# Generated by Django 5.0.3 on 2024-03-18 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_locatario_telefone_alter_pessoa_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendas_de_imoveis',
            name='valor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.imovel'),
            preserve_default=False,
        ),
    ]
