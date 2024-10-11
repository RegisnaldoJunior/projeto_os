from django.db import models
from django.core.validators import RegexValidator
from datetime import date

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=10)
    nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, validators=[RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message='CPF deve seguir o formato XXX.XXX.XXX-XX')])
    endereco = models.CharField(max_length=255)
    data_cadastro = models.DateField(default=date.today)
    telefone_fixo = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\(\d{2}\)\d{4,5}-\d{4}$', message='Telefone deve seguir o formato (XX)XXXXX-XXXX')])
    telefone_celular = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\(\d{2}\)\d{4,5}-\d{4}$', message='Telefone deve seguir o formato (XX)XXXXX-XXXX')])
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True, validators=[RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', message='CNPJ deve seguir o formato XX.XXX.XXX/XXXX-XX')])
    endereco = models.CharField(max_length=255)
    telefone_fixo = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\(\d{2}\)\d{4,5}-\d{4}$')])
    telefone_celular = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\(\d{2}\)\d{4,5}-\d{4}$')])
    email = models.EmailField()
    data_cadastro = models.DateField(default=date.today)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=10)
    nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, validators=[RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')])
    endereco = models.CharField(max_length=255)
    data_cadastro = models.DateField(default=date.today)
    telefone_fixo = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\(\d{2}\)\d{4,5}-\d{4}$')])
    telefone_celular = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\(\d{2}\)\d{4,5}-\d{4}$')])
    email = models.EmailField()
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class OrdemServico(models.Model):
    tecnico = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao_problema = models.TextField()
    data = models.DateField(default=date.today)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class ItemOrdemServico(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total_item = models.DecimalField(max_digits=10, decimal_places=2)

class ContaReceber(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True, validators=[RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$')])
    endereco = models.CharField(max_length=255)
    telefone_fixo = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\(\d{2}\)\d{4,5}-\d{4}$')])
    telefone_celular = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\(\d{2}\)\d{4,5}-\d{4}$')])
    email = models.EmailField()
    data_cadastro = models.DateField(default=date.today)

    def __str__(self):
        return self.nome


"""Clientes (Id, nome, sexo, nascimento, CPF, endereço (rua, bairro, número,
CEP), data de cadastro, telefones (Fixo, celular), e-mail)
Obs. O nome do cliente deve ser preenchido sempre – Não permitir gravação
com o nome em branco;
Os telefones devem ser mascarados (99)99999-9999
Os campos CEP e CPF também devem receber máscaras
A data atual do servidor deve ser sugerida para a data de cadastro.
Se a data de nascimento for deixada em branco, uma mensagem deve informar,
mas será permitido a gravação sem que a mesma seja preenchida;
"""