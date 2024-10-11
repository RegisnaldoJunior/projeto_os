from django.shortcuts import render, redirect
from .models import Cliente  # Certifique-se de que você tenha um modelo Cliente

def home(request):
    return render(request, 'core/home.html')

def cadastrar_cliente(request):
    if request.method == 'POST':
        # Lógica para salvar o cliente
        pass
    return render(request, 'core/cadastrar_cliente.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/listar_clientes.html', {'clientes': clientes})
