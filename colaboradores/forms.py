from django import forms


class FormColaborador(forms.Form):
    nome = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)


class FormLogin(forms.Form):
    email = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput)