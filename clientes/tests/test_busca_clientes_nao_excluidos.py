from django.test import TestCase

from clientes.models import Cliente
from clientes.gateway import busca_clientes_nao_excluidos


class BuscaClientesNaoExcluidosTests(TestCase):
    def setUp(self):
        self.cliente_excluido_1 = Cliente.objects.create(nome='Cliente excluido 1', excluido=True)
        self.cliente_excluido_2 = Cliente.objects.create(nome='Cliente excluido 2', excluido=True)
        self.cliente_ativo_1 = Cliente.objects.create(nome='Cliente ativo 1', excluido=False)
        self.cliente_ativo_2 = Cliente.objects.create(nome='Cliente ativo 2', excluido=False)


    def test_busca_clientes_nao_excluidos(self):
        result = busca_clientes_nao_excluidos().count()
        result_list = busca_clientes_nao_excluidos()

        self.assertEqual(result, 2)
        self.assertEqual(result_list[0].id, 3)
        self.assertEqual(result_list[1].nome, 'Cliente ativo 2')
