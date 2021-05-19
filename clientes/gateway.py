from clientes.models import Cliente



def busca_um_cliente(cliente_id):
    return Cliente.objects.get(id=cliente_id)


def busca_clientes_nao_excluidos():
    return Cliente.objects.filter(excluido=False)


def busca_todos_os_clientes():
    return Cliente.objects.all()


