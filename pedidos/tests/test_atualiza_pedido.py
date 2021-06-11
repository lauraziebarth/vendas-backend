from django.test import TestCase

from pedidos.serializer import PedidoSerializer
from pedidos.gateway import atualiza_pedido


class AtualizaPedidoTests(TestCase):
    def setUp(self):
        self.pedido_antigo = {'id': 1, 'cliente_id': 1, 'cliente_nome': 'Han Solo', 'condicao_pagamento': '30/60', 'total': 750009.87,
                              'itens': []}

        self.pedido_novo = {'id': 1, 'cliente_id': 1, 'cliente_nome': 'Han Solo', 'condicao_pagamento': 'a vista', 'total': 900000.00,
                            'itens': []}


    def test_atualiza_pedido(self):
        serializer_pedido_antigo = PedidoSerializer(data=self.pedido_antigo)
        if serializer_pedido_antigo.is_valid():
            serializer_pedido_antigo.save()

        pedido_id = serializer_pedido_antigo.data.get('id')

        serializer_pedido_novo = PedidoSerializer(data=self.pedido_novo)
        if serializer_pedido_novo.is_valid():
            result = atualiza_pedido(pedido_id, self.pedido_novo)

        self.assertEqual(result.id, 1)
        self.assertEqual(result.condicao_pagamento, 'a vista')
        self.assertEqual(result.total, 900000.00)
