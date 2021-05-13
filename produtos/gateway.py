from produtos.models import Produto


def busca_um_produto(produto_id):
    return Produto.objects.get(id=produto_id)

