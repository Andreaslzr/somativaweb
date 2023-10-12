from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'clientes',ClienteView)
router.register(r'funcionarios',FuncionarioView)
router.register(r'categoriaServico',CategoriaServicoView)
router.register(r'produtos',ProdutoView)
router.register(r'automovel',AutomovelView)
router.register(r'manutencao',ManutencaoView)
router.register(r'manutencaoCategoria',ManutencaoCategoriaView)
router.register(r'manutencaoProduto',ManutencaoProdutoView)
router.register(r'pagamentos',PagamentoView)
router.register(r'postoTrabalho',PostoTrabalhoView)
router.register(r'postoFuncionario',PostoFuncionarioView)
router.register(r'reservas',ReservaView)
router.register(r'disponibilidades',DisponibilidadeView)

urlpatterns = router.urls