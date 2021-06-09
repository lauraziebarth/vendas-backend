from django.test import TestCase

from clientes.models import Cliente
from clientes.gateway import busca_todos_os_clientes


class BuscaTodosOsClientesTests(TestCase):
    def setUp(self):
        self.cliente_excluido_1 = Cliente.objects.create(nome='Cliente excluido 1', excluido=True)
        self.cliente_excluido_2 = Cliente.objects.create(nome='Cliente excluido 2', excluido=True)
        self.cliente_ativo_1 = Cliente.objects.create(nome='Cliente ativo 1', excluido=False)
        self.cliente_ativo_2 = Cliente.objects.create(nome='Cliente ativo 2', excluido=False)


    def test_busca_todos_os_clientes(self):
        result = busca_todos_os_clientes().count()
        result_list = busca_todos_os_clientes()

        self.assertEqual(result, 4)
        self.assertEqual(result_list[0].id, 1)
        self.assertEqual(result_list[1].nome, 'Cliente excluido 2')
        self.assertEqual(result_list[2].excluido, False)
        self.assertEqual(result_list[3].id, 4)
