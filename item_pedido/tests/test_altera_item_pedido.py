from django.test import TestCase

from item_pedido.crud import atualiza_itens_pedido, cria_item_pedido
from pedidos.serializer import PedidoSerializer


class AlteraItensPedidoTests(TestCase):
    def setUp(self):
        self.pedido_antigo = {'id': 1, 'cliente_id': 1, 'cliente_nome': 'Han Solo', 'condicao_pagamento': '30/60', 'total': 750009.87,
                              'itens': [{'produto_id': 4, 'produto_nome': 'TIE Fighter', 'produto_multiplo': 2,
                                         'produto_preco_tabela': 75000, 'quantidade': 10, 'preco_liquido': 75000.99,
                                         'total': 750009.87, 'rentabilidade': 'great'}]}

        self.pedido_novo = {'id': 1, 'cliente_id': 1, 'cliente_nome': 'Han Solo', 'condicao_pagamento': '30/60', 'total': 750009.87,
                            'itens': [{'produto_id': 4, 'produto_nome': 'TIE Fighter', 'produto_multiplo': 2,
                                       'produto_preco_tabela': 75000, 'quantidade': 8, 'preco_liquido': 75000.99,
                                       'total': 60007.92, 'rentabilidade': 'great', 'id':1}]}

    def test_cria_item_pedido(self):
        serializer_pedido_antigo = PedidoSerializer(self.pedido_antigo)
        pedido_id_antigo = serializer_pedido_antigo.data.get('id')
        itens_antigos = serializer_pedido_antigo.data.get('itens')
        cria_item_pedido(pedido_id_antigo, itens_antigos)

        serializer_pedido_novo = PedidoSerializer(self.pedido_novo)
        pedido_id = serializer_pedido_novo.data.get('id')
        itens_novos = serializer_pedido_novo.data.get('itens')
        result = atualiza_itens_pedido(pedido_id, itens_novos)

        self.assertEqual(result['produto_nome'], 'TIE Fighter')
        self.assertEqual(result['produto_multiplo'], 2)
        self.assertEqual(result['quantidade'], 8)
        self.assertEqual(result['produto_id'], 4)
