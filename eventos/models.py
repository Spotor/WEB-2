from django.db import models

class Endereco(models.Model):
    alameda = models.CharField(max_length=128, blank=True)
    numero = models.IntegerField(blank=True)
    bairro = models.CharField(max_length=20, blank=True)
    uf = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.alameda

class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)
    endereco = models.ForeignKey(Endereco, blank=True) #

    def __str__(self):
        return self.nome + "(" + self.email + ")"

class ClienteFisico(Cliente): #herança
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.cpf

class Pedido(models.Model):
    numero = models.IntegerField()
    dataPedido = models.DateTimeField(blank=True, null=True)
    cliente = models.ForeignKey(ClienteFisico, blank=True)

    def __str__(self):
        return self.numero

class ItemPedido(models.Model):
    codigoProduto = models.CharField(max_length=15)
    nomeProduto = models.CharField(max_length=40)
    qtd = models.IntegerField()
    pedido = models.ForeignKey(Pedido, blank=True)

    def __str__(self):
        return self.codigoProduto
