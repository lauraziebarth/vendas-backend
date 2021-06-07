from rest_framework import viewsets

from produtos.gateway import busca_produtos_nao_excluidos
from produtos.serializer import ProdutoSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = busca_produtos_nao_excluidos()
    serializer_class = ProdutoSerializer


