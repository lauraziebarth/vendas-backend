from rest_framework import viewsets

from pedidos.pedido_gateway import busca_todos_os_pedidos
from pedidos.serializer import PedidoSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = busca_todos_os_pedidos()
    serializer_class = PedidoSerializer
