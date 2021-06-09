from django.test import TestCase

from produtos.models import Produto
from produtos.gateway import busca_um_produto


class BuscaUmUnicoProdutoTests(TestCase):
    def setUp(self):
        self.produto_excluido_1 = Produto.objects.create(nome='Produto excluido 1', preco_tabela=10, multiplo=5, excluido=True)
        self.produto_excluido_2 = Produto.objects.create(nome='Produto excluido 2', preco_tabela=30, multiplo=7, excluido=True)
        self.produto_ativo_1 = Produto.objects.create(nome='Produto ativo 1', preco_tabela=70, multiplo=3, excluido=False)
        self.produto_ativo_2 = Produto.objects.create(nome='Produto ativo 2', preco_tabela=40, multiplo=2, excluido=False)


    def test_busca_um_unico_produto(self):
        result = busca_um_produto(2)

        self.assertEqual(result.id, 2)
        self.assertEqual(result.nome, 'Produto excluido 2')
        self.assertEqual(result.preco_tabela, 30)
        self.assertEqual(result.multiplo, 7)
