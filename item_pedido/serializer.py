from rest_framework import serializers
from item_pedido.models import ItemPedido


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ('produto_id', 'produto_multiplo', 'produto_nome', 'produto_preco_tabela', 'quantidade', 'preco_liquido',
                  'rentabilidade', 'total', 'pedido_id')