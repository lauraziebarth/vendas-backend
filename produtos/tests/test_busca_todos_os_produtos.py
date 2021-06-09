from django.test import TestCase

from produtos.models import Produto
from produtos.gateway import busca_todos_os_produtos


class BuscaTodosOsProdutosTests(TestCase):
    def setUp(self):
        self.produto_excluido_1 = Produto.objects.create(nome='Produto excluido 1', preco_tabela=10, multiplo=5, excluido=True)
        self.produto_excluido_2 = Produto.objects.create(nome='Produto excluido 2', preco_tabela=30, multiplo=7, excluido=True)
        self.produto_ativo_1 = Produto.objects.create(nome='Produto ativo 1', preco_tabela=70, multiplo=3, excluido=False)
        self.produto_ativo_2 = Produto.objects.create(nome='Produto ativo 2', preco_tabela=40, multiplo=2, excluido=False)


    def test_busca_todos_os_produtos(self):
        result = busca_todos_os_produtos().count()
        result_list = busca_todos_os_produtos()

        self.assertEqual(result, 4)
        self.assertEqual(result_list[0].preco_tabela, 10)
        self.assertEqual(result_list[1].nome, 'Produto excluido 2')
        self.assertEqual(result_list[2].multiplo, 3)
        self.assertEqual(result_list[3].excluido, False)
