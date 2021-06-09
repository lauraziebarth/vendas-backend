from django.test import TestCase

from clientes.models import Cliente
from clientes.gateway import busca_um_cliente


class BuscaUnicoClienteTests(TestCase):
    def setUp(self):
        self.cliente_excluido_1 = Cliente.objects.create(nome='Cliente excluido 1', excluido=True)
        self.cliente_excluido_2 = Cliente.objects.create(nome='Cliente excluido 2', excluido=True)
        self.cliente_ativo_1 = Cliente.objects.create(nome='Cliente ativo 1', excluido=False)
        self.cliente_ativo_2 = Cliente.objects.create(nome='Cliente ativo 2', excluido=False)


    def test_busca_um_unico_cliente(self):
        result = busca_um_cliente(3)

        self.assertEqual(result.id, 3)
        self.assertEqual(result.nome, 'Cliente ativo 1')
        self.assertEqual(result.excluido, False)
