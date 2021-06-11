from django.test import TestCase

from item_pedido.crud import cria_item_pedido
from item_pedido.gateway import busca_todos_os_itens_de_um_pedido
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
        cria_item_pedido(pedido_id, itens)

        result = busca_todos_os_itens_de_um_pedido(pedido_id).count()
        result_list = busca_todos_os_itens_de_um_pedido(pedido_id)
        self.assertEqual(result, 1)
        self.assertEqual(result_list[0].id, 1)
        self.assertEqual(result_list[0].produto_id, 4)
        self.assertEqual(result_list[0].produto_nome, 'TIE Fighter')
        self.assertEqual(result_list[0].quantidade, 10)

