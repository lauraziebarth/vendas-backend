from django.test import TestCase

from pedidos.models import Pedido
from item_pedido.models import ItemPedido
from clientes.models import Cliente
from produtos.models import Produto
from pedidos.gateway import busca_um_pedido


class BuscaUmPedidoTests(TestCase):
    def setUp(self):
        self.cliente_1 = Cliente.objects.create(nome='Cliente 1', excluido=False)
        self.cliente_2 = Cliente.objects.create(nome='Cliente 2', excluido=False)

        self.produto_1 = Produto.objects.create(nome='Produto 1', preco_tabela=10, multiplo=5, excluido=True)
        self.produto_2 = Produto.objects.create(nome='Produto 2', preco_tabela=30, multiplo=7, excluido=True)
        self.produto_3 = Produto.objects.create(nome='Produto 3', preco_tabela=70, multiplo=3, excluido=False)
        self.produto_4 = Produto.objects.create(nome='Produto 4', preco_tabela=40, multiplo=2, excluido=False)

        self.pedido_1 = Pedido.objects.create(condicao_pagamento='a vista', cliente_id=self.cliente_1.id, cliente_nome=self.cliente_1.nome, total=100)
        self.pedido_2 = Pedido.objects.create(condicao_pagamento='30/60', cliente_id=self.cliente_2.id, cliente_nome=self.cliente_2.nome, total=200)

        self.item_pedido_1 = ItemPedido.objects.create(produto_id=self.produto_1.id, produto_multiplo=self.produto_1.multiplo, produto_nome=self.produto_1.nome,
                                                       produto_preco_tabela=self.produto_1.preco_tabela, quantidade=5, preco_liquido=15,
                                                       pedido_id=self.pedido_1.id)
        self.item_pedido_2 = ItemPedido.objects.create(produto_id=self.produto_2.id, produto_multiplo=self.produto_2.multiplo, produto_nome=self.produto_2.nome,
                                                       produto_preco_tabela=self.produto_2.preco_tabela, quantidade=7, preco_liquido=30,
                                                       pedido_id=self.pedido_1.id)
        self.item_pedido_3 = ItemPedido.objects.create(produto_id=self.produto_3.id, produto_multiplo=self.produto_3.multiplo, produto_nome=self.produto_3.nome,
                                                       produto_preco_tabela=self.produto_3.preco_tabela, quantidade=3, preco_liquido=70,
                                                       pedido_id=self.pedido_2.id)
        self.item_pedido_4 = ItemPedido.objects.create(produto_id=self.produto_4.id, produto_multiplo=self.produto_4.multiplo, produto_nome=self.produto_4.nome,
                                                       produto_preco_tabela=self.produto_4.preco_tabela, quantidade=2, preco_liquido=45,
                                                       pedido_id=self.pedido_2.id)


    def test_busca_um_pedido(self):
        result = busca_um_pedido(self.pedido_1.id)

        self.assertEqual(result['condicao_pagamento'], 'a vista')
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['cliente_id'], self.cliente_1.id)