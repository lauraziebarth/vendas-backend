class ItemPedidoGateway(object):
    def buscar_itens_do_pedido(self, pedido_id):
        raise NotImplementedError

    def obter_item_pedido_por_id(self, item_pedido_id):
        raise NotImplementedError

    def buscar_itens_exceto_itens_que_tiveram_preco_liquido_alterado_manualmente(self, pedido_id):
        raise NotImplementedError

    def produto_existe_no_pedido(self, produto_id, pedido_id):
        raise NotImplementedError

    def criar_item_no_pedido(self, item_pedido, pedido, atualizar_pedido=False, descontos_de_politicas_comerciais=None):
        raise NotImplementedError

    def excluir_item_no_pedido(self, pedido, item_pedido_id):
        raise NotImplementedError

    def alterar_item_no_pedido(self, pedido, item_pedido_id, quantidade, informacoes_adicionais, itens_de_grade=None, descontos=None):
        raise NotImplementedError

    def salvar_item_completo_no_pedido(self, item):
        raise NotImplementedError

    def excluir_itens_do_pedido(self, pedido_id, itens_ids=None):
        raise NotImplementedError


def alterar_item_pedido(filtros, **atributos):
    from pedidos.models import ItemPedido
    return alterar(ItemPedido, filtros, **atributos)
