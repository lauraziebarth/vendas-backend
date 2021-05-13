from produtos.gateway import busca_um_produto
from produtos.models import Produto
from datetime import datetime


def cria_produto(nome, preco_tabela, multiplo):
    produto = Produto()
    produto.nome = nome
    produto.preco_tabela = preco_tabela
    produto.multiplo = multiplo
    produto.save()

def alterar_produto(produto_id, nome, preco_tabela, multiplo):
    produto = busca_um_produto(produto_id)
    produto.nome = nome
    produto.preco_tabela = preco_tabela
    produto.multiplo = multiplo
    produto.ultima_alteracao = datetime.now()
    produto.save()


def excluir_produto(produto_id):
    produto = busca_um_produto(produto_id)
    produto.excluido = True
    produto.ultima_alteracao = datetime.now()
    produto.save()


