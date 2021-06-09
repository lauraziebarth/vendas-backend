from django.test import TestCase

from produtos.models import Produto
from produtos.gateway import busca_produtos_nao_excluidos


class BuscaProdutosNaoExcluidosTests(TestCase):
    def setUp(self):
        self.produto_excluido_1 = Produto.objects.create(nome='Produto excluido 1', preco_tabela=10, multiplo=5, excluido=True)
        self.produto_excluido_2 = Produto.objects.create(nome='Produto excluido 2', preco_tabela=30, multiplo=7, excluido=True)
        self.produto_ativo_1 = Produto.objects.create(nome='Produto ativo 1', preco_tabela=70, multiplo=3, excluido=False)
        self.produto_ativo_2 = Produto.objects.create(nome='Produto ativo 2', preco_tabela=40, multiplo=2, excluido=False)


    def test_busca_produtos_nao_excluidos(self):
        result = busca_produtos_nao_excluidos().count()
        result_list = busca_produtos_nao_excluidos()

        self.assertEqual(result, 2)
        self.assertEqual(result_list[0].id, 3)
        self.assertEqual(result_list[1].id, 4)
        self.assertEqual(result_list[0].nome, 'Produto ativo 1')
        self.assertEqual(result_list[1].nome, 'Produto ativo 2')