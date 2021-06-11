from item_pedido.gateway import busca_um_item_pedido_por_id, busca_todos_os_itens_de_um_pedido
from item_pedido.models import ItemPedido


def cria_item_pedido(pedido_id, itens):
    for item in itens:
        item_pedido = ItemPedido()
        item_pedido.produto_id = item.get('produto_id')
        item_pedido.produto_multiplo = item.get('produto_multiplo')
        item_pedido.produto_nome = item.get('produto_nome')
        item_pedido.produto_preco_tabela = item.get('produto_preco_tabela')
        item_pedido.quantidade = item.get('quantidade')
        item_pedido.preco_liquido = item.get('preco_liquido')
        item_pedido.rentabilidade = item.get('rentabilidade')
        item_pedido.total = item.get('total')
        item_pedido.pedido_id = pedido_id
        item_pedido.save()
        return item_pedido


def atualiza_itens_pedido(pedido_id, itens_novos):
    itens_antigos = busca_todos_os_itens_de_um_pedido(pedido_id)
    novos_itens_ids = []
    itens_antigos_ids = []

    for item_novo in itens_novos:
        novos_itens_ids.append(item_novo['id'])

        item = busca_um_item_pedido_por_id(item_novo['id'])
        item.produto_id = item_novo['produto_id']
        item.produto_multiplo = item_novo['produto_multiplo']
        item.produto_nome = item_novo['produto_nome']
        item.produto_preco_tabela = item_novo['produto_preco_tabela']
        item.quantidade = item_novo['quantidade']
        item.preco_liquido = item_novo['preco_liquido']
        item.rentabilidade = item_novo['rentabilidade']
        item.total = item_novo['total']
        item.pedido_id = pedido_id
        item.save()

    for item in itens_antigos:
        itens_antigos_ids.append(item.id)

        if item.id not in novos_itens_ids:
            item = busca_um_item_pedido_por_id(item.id)
            item.excluido = True
            item.save()

    for item in itens_novos:
        print(item)
        if item['id'] not in itens_antigos_ids:
            item_criado = ItemPedido()
            item_criado.produto_id = item['produto_id']
            item_criado.produto_multiplo = item['produto_multiplo']
            item_criado.produto_nome = item['produto_nome']
            item_criado.produto_preco_tabela = item['produto_preco_tabela']
            item_criado.quantidade = item['quantidade']
            item_criado.preco_liquido = item['preco_liquido']
            item_criado.rentabilidade = item['rentabilidade']
            item_criado.total = item['total']
            item_criado.pedido_id = pedido_id
            item_criado.save()
