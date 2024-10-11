from django.urls import path
from .views import cadastrar_cliente, listar_clientes, home  # Certifique-se de que listar_clientes está aqui

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar-cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar-clientes/', listar_clientes, name='listar_clientes'),  # Aqui deve estar a mesma função
]
