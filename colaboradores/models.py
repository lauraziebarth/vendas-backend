from django.db import models


class Colaborador(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    excluido = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    ultima_alteracao = models.DateTimeField(auto_now=True)