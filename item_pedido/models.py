from django.db import models

from produtos.models import Produto
from pedidos.models import Pedido


class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    produto_multiplo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    produto_nome = models.CharField(max_length=100)
    produto_preco_tabela = models.DecimalField(max_digits=12, decimal_places=2)

    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_liquido = models.DecimalField(max_digits=12, decimal_places=2)
    excluido = models.BooleanField(default=False)

    pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    ultima_alteracao = models.DateTimeField(auto_now=True)