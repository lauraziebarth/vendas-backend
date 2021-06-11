from rest_framework import serializers

from pedidos.models import Pedido
from item_pedido.serializer import ItemPedidoSerializer



class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(read_only=True, many=True)

    class Meta:
        model = Pedido
        fields = ('id', 'cliente', 'cliente_nome', 'condicao_pagamento', 'total', 'itens')
