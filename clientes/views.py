from clientes.gateway import busca_todos_os_clientes

from rest_framework import viewsets
from clientes.serializer import ClienteSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = busca_todos_os_clientes()
    serializer_class = ClienteSerializer


