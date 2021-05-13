from django import forms


class FormProduto(forms.Form):
    nome = forms.CharField(max_length=100)
    preco_tabela= forms.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0)
    multiplo = forms.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
