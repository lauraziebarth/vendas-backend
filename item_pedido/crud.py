from item_pedido.models import ItemPedido


def cria_item_pedido(pedido_id, itens):
    for item in itens:
        item_pedido = ItemPedido()
        item_pedido.produto_id = item.get('produto_id')
        item_pedido.multiplo = item.get('multiplo')
        item_pedido.produto_nome = item.get('produto_nome')
        item_pedido.produto_preco_tabela = item.get('produto_preco_tabela')
        item_pedido.quantidade = item.get('quantidade')
        item_pedido.preco_liquido = item.get('preco_liquido')
        item_pedido.rentabilidade_produto = item.get('rentabilidade_produto')
        item_pedido.pedido_id = pedido_id
        item_pedido.save()



