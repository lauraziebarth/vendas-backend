from clientes.gateway import busca_um_cliente
from clientes.models import Cliente
from datetime import datetime


def criar_cliente(nome):
    cliente = Cliente()
    cliente.nome = nome
    cliente.save()

def alterar_cliente(cliente_id, nome):
    cliente = busca_um_cliente(cliente_id)
    cliente.nome = nome
    cliente.ultima_alteracao = datetime.now()
    cliente.save()


def excluir_cliente(cliente_id):
    cliente = busca_um_cliente(cliente_id)
    cliente.excluido = True
    cliente.ultima_alteracao = datetime.now()
    cliente.save()


