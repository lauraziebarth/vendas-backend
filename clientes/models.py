from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    excluido = models.BooleanField(default=False)
    ultima_alteracao = models.DateTimeField(auto_now=True)

