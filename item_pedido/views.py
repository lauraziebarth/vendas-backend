from rest_framework import viewsets
from rest_framework.response import Response

from item_pedido.gateway import busca_todos_os_itens_de_um_pedido, busca_um_item_pedido_por_id, busca_todos_os_itens
from item_pedido.serializer import ItemPedidoSerializer


class ItensPedidoViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = busca_todos_os_itens()
        serializer_class = ItemPedidoSerializer(queryset, many=True)
        return Response(serializer_class.data)


    def retrieve(self, request, fk=None):
        queryset = busca_todos_os_itens_de_um_pedido(fk)
        serializer_class = ItemPedidoSerializer(queryset, many=True)
        return Response(serializer_class.data)


    def retrieve(self, request, pk=None):
        queryset = busca_um_item_pedido_por_id(pk)
        serializer_class = ItemPedidoSerializer(queryset)
        return Response(serializer_class.data)

