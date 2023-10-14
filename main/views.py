from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from datetime import timedelta, datetime

from django_filters.rest_framework import DjangoFilterBackend
from .customFilters import *
from rest_framework import filters
from django.db.models import Avg

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
def strToDate(strDate):
    return datetime.strptime(strDate, '%Y-%m-%d').date()

class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class comprarView(APIView):
    def get(self, request):
        produtos_comprar = produto.objects.get(request.data)
        if produtos_comprar['QuantEstoque'] <4:
            serializer = ProdutoSerializer(produtos_comprar, many=True)
        return Response(status=200, data=serializer.data)


class NotaMediaView(APIView):

    def get(self, request, manutencaoId = ''):
        if manutencaoId == '': return Response(status=400,data='obrigatorio passar o parametro manutençãoId')
        try:
            manutencaoFound = manutencao.objects.get(id=manutencaoId)
            serializerManutencao = ManutencaoSerializer(manutencaoFound, many=False)
            media = reserva.objects.filter(manutencaoFK=manutencaoId).aggregate(Avg('nota'))
            if media is not None: return Response(status=200, data={'media': media['nota__avg'], 'manutencao': serializerManutencao.data}) 
            else: return Response(status=404,data='não foi possivel obter a media dessa reserva')

        except manutencao.DoesNotExist:
            return Response(status=404, data='manutenção não encontrada')
    

class ClienteView(ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class  = ClienteFilter
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)

class FuncionarioView(ModelViewSet):
   queryset = funcionario.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = FuncionarioSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['nome', 'cpf', 'cep']
   ordering_fields = '__all__'
   permission_classes = (IsAuthenticated,)

class CategoriaServicoView(ModelViewSet):
   queryset = categoriaServico.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = CatServicoSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['nome',]
   ordering_fields = '__all__'
   permission_classes = (IsAuthenticated,)

class ProdutoView(ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class  = ProdutoFilter
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = pagamento.objects.all()
        else:
            queryset = 'você não possui autenticação para ver essa informação'
        return queryset

class AutomovelView(ModelViewSet):
    queryset = automovel.objects.all()
    serializer_class = AutomovelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class  = AutomovelFilter
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)

class ManutencaoView(ModelViewSet):
   queryset = manutencao.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = ManutencaoSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['automovelFK','funcionarioFK']
   ordering_fields = '__all__'
   permission_classes = (IsAuthenticated,)

   def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = manutencao.objects.all()
        else:
            queryset = manutencao.objects.filter(automovelFK__clienteFK__nome=user.username)
        return queryset 
   
   def create(self, request, *args, **kwargs): 
        data = request.data

        if user.is_superuser or funcionario.id:
            super(ReservaView, self).create(request,*args,**kwargs)
        else:
            return Response(status=500, data='erro ao salvar manutençao')
   
class ManutencaoCategoriaView(ModelViewSet):
   queryset = manutencao_categoria.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = ManutencaoCatSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['manutencaoFK',]
   ordering_fields = '__all__'
   permission_classes = (IsAuthenticated,)

class ManutencaoProdutoView(ModelViewSet):
   queryset = manutencao_produto.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = ManutencaoProdutoSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['manutencaoFK',]
   ordering_fields = '__all__'
   permission_classes = (IsAuthenticated,)

class PagamentoView(ModelViewSet):
   queryset = pagamento.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = PagamentoSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['categoria','descricao','status']
   ordering_fields = '__all__'
   permission_classes = (IsAuthenticated,)

   def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = pagamento.objects.all()
        else:
            queryset = pagamento.objects.filter(manutencaoFK__automovelFK__clienteFK__nome=user.username)
        return queryset 
   
class PostoTrabalhoView(ModelViewSet):
   queryset = postoTrabalho.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = PostoTrabalhoSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['descricao',]
   ordering_fields = '__all__'
   permission_classes = (IsAdminUser,)

class PostoFuncionarioView(ModelViewSet):
   queryset = posto_funcionario.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = PostoFuncionarioSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['postoFK','funcionarioFK']
   ordering_fields = '__all__'
   permission_classes = (IsAdminUser,)

class ReservaView(ModelViewSet):
   queryset = reserva.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = ReservaSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['clienteFK','postoFK','dia']
   ordering_fields = '__all__'
   permission_classes = (IsAuthenticated,)

   def create(self, request, *args, **kwargs): 
        data = request.data
        diaEscolhido = strToDate(data['dia'])
        availabilities = []

        availability = disponibilidade.objects.filter(postoFK=data['postoFK']).filter(dia=diaEscolhido).filter(reservaFK=None)
        if availability <3: 
                return Response(status=409,data='essa data nã está disponivel, considere escolher outra data')
        
        availabilities.append(availability)

        savedReservaResponse = super(ReservaView, self).create(request,*args,**kwargs)
        if savedReservaResponse.status_code == 201:   
            savedReserva = reserva.objects.get(pk=savedReservaResponse.data['id'])
            for availability in availabilities:
                availability.reservaFK = savedReserva
                availability.save()
            return Response(status=201,data=savedReservaResponse.data)
        else:
            return Response(status=500,data='Erro ao salvar reserva')

class DisponibilidadeView(CustomModelViewSet):
   queryset = disponibilidade.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = DisponibilidadeSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend, filters.OrderingFilter] #usa a lib django-filter
   filterset_fields = ['postoFK','reservaFK','dia']
   ordering_fields = '__all__'
   permission_classes = (IsAuthenticated,)

   def create(self, request, *args, **kwargs): 
        data = request.data

        if user.is_superuser:
            super(ReservaView, self).create(request,*args,**kwargs)
        else:
            return Response(status=500, data='erro ao salvar disponibilidade')