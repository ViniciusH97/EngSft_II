# Generated by Django 5.0.3 on 2024-03-12 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_logradouros_numero'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cargos',
            new_name='Bairro',
        ),
        migrations.RenameModel(
            old_name='Tipos_imoveis',
            new_name='Cargo',
        ),
        migrations.RenameModel(
            old_name='Cidades',
            new_name='Cidade',
        ),
        migrations.RenameModel(
            old_name='Locacao_de_imoveis',
            new_name='Locacao_de_imovel',
        ),
        migrations.RenameModel(
            old_name='Logradouros',
            new_name='Logradouro',
        ),
        migrations.RenameModel(
            old_name='Pessoas',
            new_name='Pessoa',
        ),
        migrations.RenameModel(
            old_name='Bairros',
            new_name='Tipo_imovel',
        ),
        migrations.AlterModelOptions(
            name='bairro',
            options={'verbose_name_plural': 'Bairros'},
        ),
        migrations.AlterModelOptions(
            name='cargo',
            options={'verbose_name_plural': 'Cargos'},
        ),
        migrations.AlterModelOptions(
            name='cidade',
            options={'verbose_name_plural': 'Cidades'},
        ),
        migrations.AlterModelOptions(
            name='locacao_de_imovel',
            options={'verbose_name_plural': 'Locação de Imóveis'},
        ),
        migrations.AlterModelOptions(
            name='logradouro',
            options={'verbose_name_plural': 'Logradouros'},
        ),
        migrations.AlterModelOptions(
            name='pessoa',
            options={'verbose_name_plural': 'Pessoas'},
        ),
        migrations.AlterModelOptions(
            name='tipo_imovel',
            options={'verbose_name_plural': 'Tipos imoveis'},
        ),
        migrations.RenameField(
            model_name='imoveis',
            old_name='valo_de_venda',
            new_name='valor_de_venda',
        ),
    ]