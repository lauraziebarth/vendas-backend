from pedidos.models import Pedido


def busca_um_pedido(pedido_id):
    return Pedido.objects.get(id=pedido_id)


def busca_todos_os_pedidos():
    return Pedido.objects.all()

