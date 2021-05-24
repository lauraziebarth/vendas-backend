from django.db import models

from clientes.models import Cliente


class Pedido(models.Model):
    numero = models.IntegerField(db_index=True)
    data_emissao = models.DateTimeField(auto_now=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    condicao_pagamento = models.CharField(max_length=100, blank=True, null=True)

    cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.DO_NOTHING)
    cliente_nome = models.CharField(null=True, blank=True, max_length=200)

    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


