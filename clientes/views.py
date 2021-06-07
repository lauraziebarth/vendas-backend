from rest_framework import viewsets
from clientes.serializer import ClienteSerializer

from clientes.gateway import busca_clientes_nao_excluidos


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = busca_clientes_nao_excluidos()
    serializer_class = ClienteSerializer


