from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse

from clientes.crud import criar_cliente, alterar_cliente, excluir_cliente
from clientes.forms import FormCliente
from clientes.gateway import busca_clientes_nao_excluidos, busca_um_cliente
from colaboradores.models import Colaborador


class ListarClientes(LoginRequiredMixin, View):
    def get(self, request):
        usuario_logado_id = request.user.id
        colaborador_logado = Colaborador.objects.get(user_id=usuario_logado_id)

        clientes = busca_clientes_nao_excluidos()
        return render(request, 'listar_clientes.html', {'clientes': clientes, 'colaborador_logado': colaborador_logado })


class CadastrarCliente(LoginRequiredMixin, View):
    def get(self, request):
        form = FormCliente()
        usuario_logado_id = request.user.id
        colaborador_logado = Colaborador.objects.get(user_id=usuario_logado_id)
        return render(request, 'cadastrar_dispositivo.html', {'form': form, 'colaborador_logado': colaborador_logado})


    def post(self, request):
        form = FormCliente(request.POST)

        if not form.is_valid():
            return render(request, 'cadastrar_cliente.html', {'form': form})

        nome = form.cleaned_data['nome']

        criar_cliente(nome)

        return redirect(reverse('listar_clientes.html'))


class AlterarCliente(LoginRequiredMixin, View):
    def get(self, request, cliente_id=None):
        cliente = busca_um_cliente(cliente_id)
        form = FormCliente(initial={'id': cliente.id, 'nome': cliente.nome})
        return render(request, 'alterar_cliente.html', {'form': form, 'cliente_id': cliente_id})

    def post(self, request, cliente_id=None):
        form = FormCliente(request.POST)

        if not form.is_valid():
            return render(request, 'alterar_cliente.html', {'form': form, 'cliente_id': cliente_id})

        nome = form.cleaned_data['nome']

        alterar_cliente(cliente_id, nome)

        return redirect(reverse('listar_clientes'))


class ExcluirCliente(LoginRequiredMixin, View):
    def get(self, cliente_id=None):
        excluir_cliente(cliente_id)
        return redirect(reverse('listar_clientes'))
