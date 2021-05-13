from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco_tabela = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0)
    multiplo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    excluido = models.BooleanField(default=False)
    ultima_alteracao = models.DateTimeField(auto_now=True)

