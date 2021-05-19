from produtos.models import Produto


def busca_um_produto(produto_id):
    return Produto.objects.get(id=produto_id)


def busca_todos_os_produtos():
    return Produto.objects.all()
