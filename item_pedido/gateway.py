from item_pedido.models import ItemPedido


def busca_todos_os_itens_de_um_pedido(pedido_id):
    return ItemPedido.objects.filter(pedido_id=pedido_id)


def busca_um_item_pedido_por_id(id):
    return ItemPedido.objects.get(id=id)


def busca_todos_os_itens():
    return ItemPedido.objects.all()

