from django.db import models
from app.models import *


# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.nome

class Tipo_logradouro(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Bairro(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Bairros"

    def __str__(self):
        return self.nome
    
class Logradouro(models.Model):
    nome = models.CharField(max_length=30)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=30)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Logradouros"

    def __str__(self):
        return self.nome
    
class UF(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    

class Cidade(models.Model):
    nome = models.CharField(max_length=30)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=20)
    data_nasc = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return f'{self.nome} {self.cpf} {self.rg} {self.data_nasc} {self.email} {self.cidade}'
        
class Tipo_imovel(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Tipos imoveis"

    def __str__(self):
        return self.nome
    
class Imovel(models.Model):
    nome = models.CharField(max_length=30)
    tipo_imovel = models.ForeignKey(Tipo_imovel, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=40)
    area_construida = models.CharField(max_length=30)
    quantidade_comodos = models.IntegerField()
    cor = models.CharField(max_length=10)
    quantidade_vagas_garagem = models.IntegerField()
    tipo_logradouro = models.ForeignKey(Tipo_logradouro, on_delete=models.CASCADE)
    logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)
    cep = models.CharField(max_length=20)
    valor_de_venda = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Imóveis"

    def __str__(self):
        return f'{self.nome} {self.tipo_imovel} {self.descricao} {self.area_construida} {self.quantidade_comodos} {self.cor} {self.quantidade_vagas_garagem} {self.tipo_logradouro} {self.logradouro} {self.bairro} {self.cidade} {self.uf} {self.cep} {self.valor_de_venda}'    

class Locatario(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)  
    endereco = models.TextField()  
    email = models.EmailField() 

    def __str__(self):
        return f'{self.nome} {self.telefone} {self.endereco} {self.email}'

    
class Vendas_de_imoveis(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Locacao_de_imovel(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.TextField()  
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)  
    data_inicio_contrato = models.DateField()  
    data_fim_contrato = models.DateField() 

    class Meta:
        verbose_name_plural = "Locação de Imóveis"

    def __str__(self):
        return f'{self.nome} {self.endereco} {self.valor_aluguel} {self.data_fim_contrato} {self.data_fim_contrato}' 

class Contrato_de_Locacao(models.Model):
    locatario = models.ForeignKey(Pessoa, related_name='contratos_de_locacao', on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_do_aluguel = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Contratos de Locação/Vendas"

    def __str__(self):
        return f'Contrato de Locação de {self.locatario.nome}'

class Funcionario(models.Model):
    pessoa = models.ForeignKey(Pessoa, related_name='funcionarios', on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return f'Funcionário: {self.pessoa.nome}'


class Locador(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    tipo_do_imovel = models.ForeignKey(Tipo_imovel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Locadores"

    def __str__(self):
        return f'{self.pessoa.nome} {self.pessoa.telefone} {self.imovel.nome} {self.imovel.tipo_imovel}'
    

