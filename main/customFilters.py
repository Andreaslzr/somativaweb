from rest_framework import filters
import django_filters

from .models import *

class ClienteFilter(django_filters.FilterSet):
   nome = django_filters.CharFilter(lookup_expr='icontains')
   cpf = django_filters.CharFilter(lookup_expr='icontains')
   telefone = django_filters.CharFilter(lookup_expr='icontains')
   endereco = django_filters.CharFilter(lookup_expr='icontains')
   cep = django_filters.CharFilter(lookup_expr='icontains')

   class Meta:
      model = cliente
      fields = ['nome','cpf','telefone','endereco','cep']

class ProdutoFilter(django_filters.FilterSet):
   nome = django_filters.CharFilter(lookup_expr='icontains')
   codigoFabricante = django_filters.CharFilter(lookup_expr='icontains')
   nomeFabricante = django_filters.CharFilter(lookup_expr='icontains')
   valorCompra = django_filters.RangeFilter()
   valorVenda = django_filters.RangeFilter()

   class Meta:
      model = produto
      fields = ['nome','codigoFabricante','nomeFabricante','valorCompra','valorVenda']

class AutomovelFilter(django_filters.FilterSet):
   categoria = django_filters.CharFilter(lookup_expr='icontains')
   marca = django_filters.CharFilter(lookup_expr='icontains')
   modelo = django_filters.CharFilter(lookup_expr='icontains')
   ano = django_filters.CharFilter(lookup_expr='icontains')

   class Meta:
      model = automovel
      fields = ['categoria','marca','modelo','ano']