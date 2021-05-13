from django import forms


class FormCliente(forms.Form):
    nome = forms.CharField(max_length=200)
