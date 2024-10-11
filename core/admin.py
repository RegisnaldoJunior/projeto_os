from django.contrib import admin
from .models import Cliente, Fornecedor, Produto, Marca, Funcionario, Cargo, OrdemServico, ItemOrdemServico, ContaReceber, Empresa

admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Marca)
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(OrdemServico)
admin.site.register(ItemOrdemServico)
admin.site.register(ContaReceber)
admin.site.register(Empresa)
