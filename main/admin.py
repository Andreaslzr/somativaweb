from django.contrib import admin
from .models import *
# Register your models here.

class adminClientes(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(cliente, adminClientes)

class adminFuncionarios(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(funcionario, adminFuncionarios)

class adminCategoria(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(categoriaServico, adminCategoria)

class adminProduto(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(produto, adminProduto)

class adminAutomovel(admin.ModelAdmin):
    list_display = ('id', 'categoria','marca','modelo')
    list_display_links = ('id', 'marca','modelo')
    search_fields = ('modelo',)
    list_per_page = 10

admin.site.register(automovel, adminAutomovel)

class adminManutencao(admin.ModelAdmin):
    list_display = ('id', 'automovelFK')
    list_display_links = ('id', 'automovelFK',)
    search_fields = ('automovelFK',)
    list_per_page = 10

admin.site.register(manutencao, adminManutencao)

class adminManutencao_categoria(admin.ModelAdmin):
    list_display = ('id', 'manutencaoFK')
    list_display_links = ('id', 'manutencaoFK',)
    search_fields = ('manutencaoFK',)
    list_per_page = 10

admin.site.register(manutencao_categoria, adminManutencao_categoria)

class adminManutencao_produto(admin.ModelAdmin):
    list_display = ('id', 'manutencaoFK')
    list_display_links = ('id', 'manutencaoFK',)
    search_fields = ('manutencaoFK',)
    list_per_page = 10

admin.site.register(manutencao_produto, adminManutencao_produto)

class adminPagamento(admin.ModelAdmin):
    list_display = ('id', 'categoria','descricao')
    list_display_links = ('id', 'categoria','descricao')
    search_fields = ('categoria','descricao')
    list_per_page = 10

admin.site.register(pagamento, adminPagamento)

class adminPosto(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao',)
    search_fields = ('descricao',)
    list_per_page = 10

admin.site.register(postoTrabalho, adminPosto)

class adminPosto_funcionario(admin.ModelAdmin):
    list_display = ('id', 'postoFK','funcionarioFK')
    list_display_links = ('id', 'postoFK','funcionarioFK')
    search_fields = ('postoFK',)
    list_per_page = 10

admin.site.register(posto_funcionario, adminPosto_funcionario)

class adminReserva(admin.ModelAdmin):
    list_display = ('id', 'clienteFK')
    list_display_links = ('id', 'clienteFK',)
    search_fields = ('clienteFK',)
    list_per_page = 10

admin.site.register(reserva, adminReserva)

class adminDisponibilidade(admin.ModelAdmin):
    list_display = ('id', 'postoFK')
    list_display_links = ('id', 'postoFK',)
    search_fields = ('postoFK',)
    list_per_page = 10

admin.site.register(disponibilidade, adminDisponibilidade)