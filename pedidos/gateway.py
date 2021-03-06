from item_pedido.crud import atualiza_itens_pedido
from pedidos.models import Pedido
from item_pedido.gateway import busca_todos_os_itens_de_um_pedido
from itertools import chain


def busca_um_pedido(pedido_id):
    buscar_itens = busca_todos_os_itens_de_um_pedido(pedido_id).values()
    buscar_pedido = Pedido.objects.filter(id=pedido_id).values()
    lista_pedido_e_itens = list(chain(buscar_pedido, buscar_itens))
    pedido = lista_pedido_e_itens[0]
    pedido_itens = lista_pedido_e_itens[1:]
    pedido['itens'] = pedido_itens
    return pedido


def busca_todos_os_pedidos():
    return Pedido.objects.all()


def atualiza_pedido(pedido_id, pedido_novo):
    pedido = Pedido.objects.get(id=pedido_id)
    pedido.condicao_pagamento = pedido_novo['condicao_pagamento']
    pedido.total = pedido_novo['total']
    pedido.save()

    atualiza_itens_pedido(pedido_id, pedido_novo['itens'])

    return pedido
