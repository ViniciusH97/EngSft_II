from django.db import models

# Create your models here.

class Cargos(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Tipo_logradouro(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Bairros(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
class Logradouros(models.Model):
    nome = models.CharField(max_length=30)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=30)
    bairro = models.ForeignKey(Bairros, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
    
class UF(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    

class Cidades(models.Model):
    nome = models.CharField(max_length=30)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Pessoas(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=20)
    data_nasc = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Tipos_imoveis(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
class imoveis(models.Model):
    nome = models.CharField(max_length=30)
    tipo_imovel = models.ForeignKey(Tipos_imoveis, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=40)
    area_construida = models.CharField(max_length=30)
    quantidade_comodos = models.IntegerField()
    cor = models.CharField(max_length=10)
    quantidade_vagas_garagem = models.IntegerField()
    tipo_logradouro = models.ForeignKey(Tipo_logradouro, on_delete=models.CASCADE)
    logradouro = models.ForeignKey(Logradouros, on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairros, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)
    cep = models.CharField(max_length=20)
    valo_de_venda = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nome
    

class Locatario(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)  
    endereco = models.TextField()  
    email = models.EmailField() 

    def __str__(self):
        return self.nome

    
class Vendas_de_imoveis(models.Model):
    nome = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nome

class Locacao_de_imoveis(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.TextField()  
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)  
    data_inicio_contrato = models.DateField()  
    data_fim_contrato = models.DateField() 

    def __str__(self):
        return self.nome

    
