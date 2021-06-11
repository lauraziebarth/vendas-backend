from django.test import TestCase

from item_pedido.crud import cria_item_pedido
from pedidos.serializer import PedidoSerializer


class CriaItemPedidoTests(TestCase):
    def setUp(self):

        self.pedido = {'id': 1, 'cliente_id': 1, 'cliente_nome': 'Han Solo', 'condicao_pagamento': '30/60', 'total': 750009.87,
                             'itens': [{'produto_id': 4, 'produto_nome': 'TIE Fighter', 'produto_multiplo': 2,
                                        'produto_preco_tabela': 75000, 'quantidade': 10, 'preco_liquido': 75000.99,
                                        'total': 750009.87, 'rentabilidade': 'great'}]}


    def test_cria_item_pedido(self):
        serializer_pedido = PedidoSerializer(self.pedido)
        pedido_id = serializer_pedido.data.get('id')
        itens = serializer_pedido.data.get('itens')
        result = cria_item_pedido(pedido_id, itens)

        self.assertEqual(result.produto_nome, 'TIE Fighter')
        self.assertEqual(result.produto_multiplo, 2)
        self.assertEqual(result.quantidade, 10)
        self.assertEqual(result.produto_id, 4)

