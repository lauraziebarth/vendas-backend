"""vendas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from clientes.views import ClientesViewSet
from item_pedido.views import ItensPedidoViewSet
from produtos.views import ProdutosViewSet
from pedidos.views import PedidosViewSet

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('produtos', ProdutosViewSet, basename='Produtos')
router.register('pedidos', PedidosViewSet, basename='Pedidos')
router.register('item_pedido', ItensPedidoViewSet, basename='ItensPedido')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
