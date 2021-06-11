from django.test import TestCase

from item_pedido.crud import atualiza_itens_pedido, cria_item_pedido, busca_todos_os_itens_de_um_pedido
from pedidos.serializer import PedidoSerializer


class AlteraItensPedidoTests(TestCase):
    def setUp(self):
        self.pedido_antigo = {'id': 1, 'cliente_id': 1, 'cliente_nome': 'Han Solo', 'condicao_pagamento': '30/60', 'total': 750009.87,
                              'itens': [{'produto_id': 4, 'produto_nome': 'TIE Fighter', 'produto_multiplo': 2,
                                         'produto_preco_tabela': 75000, 'quantidade': 10, 'preco_liquido': 75000.99,
                                         'total': 750009.87, 'rentabilidade': 'great'}]}

        self.pedido_novo = {'id': 1, 'cliente_id': 1, 'cliente_nome': 'Han Solo', 'condicao_pagamento': '30/60', 'total': 750009.87,
                            'itens': [{'produto_id': 5, 'produto_nome': 'Lightsaber', 'produto_multiplo': 2,
                                       'produto_preco_tabela': 75000, 'quantidade': 8, 'preco_liquido': 75000.99,
                                       'total': 60007.92, 'rentabilidade': 'great', 'id':1}]}

    def test_altera_itens_pedido(self):
        serializer_pedido_antigo = PedidoSerializer(self.pedido_antigo)
        pedido_id_antigo = serializer_pedido_antigo.data.get('id')
        itens_antigos = serializer_pedido_antigo.data.get('itens')
        cria_item_pedido(pedido_id_antigo, itens_antigos)

        serializer_pedido_novo = PedidoSerializer(self.pedido_novo)
        pedido_id = serializer_pedido_novo.data.get('id')
        itens_novos = serializer_pedido_novo.data.get('itens')
        atualiza_itens_pedido(pedido_id, itens_novos)

        result = busca_todos_os_itens_de_um_pedido(pedido_id).count()
        result_list = busca_todos_os_itens_de_um_pedido(pedido_id)

        self.assertEqual(result, 1)
        self.assertEqual(result_list[0].id, 1)
        self.assertEqual(result_list[0].produto_id, 5)
        self.assertEqual(result_list[0].produto_nome, 'Lightsaber')
        self.assertEqual(result_list[0].quantidade, 8)
