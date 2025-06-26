from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.cidade}/{self.estado}'
    
class Hospede(models.Model):
    nome = models.CharField(max_length=100)    
    CPF = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    data_nascimento = models.DateField()
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT) 
    

    def __str__(self):
        return self.nome
    
class Quarto(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=50)
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidade = models.CharField(max_length=20)

    def __str__(self):
        return f'Quarto {self.numero} ({self.tipo}) - {self.disponibilidade}'

class Reserva(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    hospede = models.ForeignKey(Hospede, on_delete=models.PROTECT)
    quarto = models.ForeignKey(Quarto, on_delete=models.PROTECT)

    def __str__(self):
        return f'Reserva de {self.hospede.nome} - ({self.data_inicio} a {self.data_fim})'        
    
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class ReservaServico(models.Model):
    quantidade = models.IntegerField()
    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.quantidade}x {self.servico.nome} para {self.reserva}'    
    
class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20)
    data_pagamento = models.DateField()
    reserva = models.OneToOneField(Reserva, on_delete=models.PROTECT)

    def __str__(self):
        return f'Pagamento R$ {self.valor} - {self.forma_pagamento}'    
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao = models.DateField()
    email = models.EmailField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} - {self.cargo}'    