# Generated by Django 5.1.2 on 2024-10-11 19:53

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=10)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='CPF deve seguir o formato XXX.XXX.XXX-XX', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')])),
                ('endereco', models.CharField(max_length=255)),
                ('data_cadastro', models.DateField(default=datetime.date.today)),
                ('telefone_fixo', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Telefone deve seguir o formato (XX)XXXXX-XXXX', regex='^\\(\\d{2}\\)\\d{4,5}-\\d{4}$')])),
                ('telefone_celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Telefone deve seguir o formato (XX)XXXXX-XXXX', regex='^\\(\\d{2}\\)\\d{4,5}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$')])),
                ('endereco', models.CharField(max_length=255)),
                ('telefone_fixo', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\(\\d{2}\\)\\d{4,5}-\\d{4}$')])),
                ('telefone_celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\(\\d{2}\\)\\d{4,5}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254)),
                ('data_cadastro', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(message='CNPJ deve seguir o formato XX.XXX.XXX/XXXX-XX', regex='^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$')])),
                ('endereco', models.CharField(max_length=255)),
                ('telefone_fixo', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\(\\d{2}\\)\\d{4,5}-\\d{4}$')])),
                ('telefone_celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\(\\d{2}\\)\\d{4,5}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254)),
                ('data_cadastro', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=10)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')])),
                ('endereco', models.CharField(max_length=255)),
                ('data_cadastro', models.DateField(default=datetime.date.today)),
                ('telefone_fixo', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\(\\d{2}\\)\\d{4,5}-\\d{4}$')])),
                ('telefone_celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\(\\d{2}\\)\\d{4,5}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_problema', models.TextField()),
                ('data', models.DateField(default=datetime.date.today)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='ContaReceber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ordemservico')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.IntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor_total_item', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.ordemservico')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto')),
            ],
        ),
    ]