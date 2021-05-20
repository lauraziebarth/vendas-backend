from rest_framework import viewsets

from produtos.gateway import busca_todos_os_produtos
from produtos.serializer import ProdutoSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = busca_todos_os_produtos()
    serializer_class = ProdutoSerializer


