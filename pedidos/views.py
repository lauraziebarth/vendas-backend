from rest_framework import viewsets

from item_pedido.crud import cria_item_pedido
from pedidos.gateway import busca_todos_os_pedidos, busca_um_pedido, atualiza_pedido
from pedidos.serializer import PedidoSerializer
from rest_framework.response import Response


class PedidosViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = busca_todos_os_pedidos()
        serializer_class = PedidoSerializer(queryset, many=True)
        return Response(serializer_class.data)


    def retrieve(self, request, pk=None):
        queryset = busca_um_pedido(pk)
        serializer_class = PedidoSerializer(queryset)
        return Response(serializer_class.data)


    def update(self, request, pk=None):
        serializer_pedido = PedidoSerializer(data=request.data)

        if serializer_pedido.is_valid():
            atualiza_pedido(pk, request.data)

        return Response(serializer_pedido.data)


    def create(self, request):
        serializer_pedido = PedidoSerializer(data=request.data)

        if serializer_pedido.is_valid():
            serializer_pedido.save()

        pedido_id = serializer_pedido.data.get('id')
        itens = request.data.get('itens')

        cria_item_pedido(pedido_id, itens)

        return Response(serializer_pedido.data)

