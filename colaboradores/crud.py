from colaboradores.models import Colaborador


def cria_colaborador(user_id, nome, email):
    colaborador = Colaborador()
    colaborador.user_id = user_id
    colaborador.nome = nome
    colaborador.email = email
    colaborador.save()
