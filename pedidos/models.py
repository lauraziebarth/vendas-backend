from django.db import models

from clientes.models import Cliente
from produtos.models import Produto


class Pedido(models.Model):
    numero = models.IntegerField(db_index=True)
    data_emissao = models.DateTimeField(auto_now=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    condicao_pagamento = models.CharField(max_length=100, blank=True, null=True)

    cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.DO_NOTHING)
    cliente_nome = models.CharField(null=True, blank=True, max_length=200)

    rentabilidade_pedido = models.IntegerField(blank=True, null=True)

    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_de_descontos = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    produto_multiplo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    produto_nome = models.CharField(max_length=100)
    produto_preco_tabela = models.DecimalField(max_digits=12, decimal_places=2)

    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_liquido = models.DecimalField(max_digits=12, decimal_places=2)
    rentabilidade_produto = models.IntegerField(blank=True, null=True)
    excluido = models.BooleanField(default=False)

    pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    ultima_alteracao = models.DateTimeField(auto_now=True)