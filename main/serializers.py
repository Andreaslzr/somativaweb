from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'
        many = True

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = funcionario
        fields = '__all__'
        many = True

class CatServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoriaServico
        fields = '__all__'
        many = True

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'
        many = True

class AutomovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = automovel
        fields = '__all__'
        many = True

class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = manutencao
        fields = '__all__'
        many = True

class ManutencaoCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = manutencao_categoria
        fields = '__all__'
        many = True

class ManutencaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = manutencao_produto
        fields = '__all__'
        many = True

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagamento
        fields = '__all__'
        many = True

class PostoTrabalhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = postoTrabalho
        fields = '__all__'
        many = True

class PostoFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = posto_funcionario
        fields = '__all__'
        many = True

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reserva
        fields = '__all__'
        many = True

class DisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = disponibilidade
        fields = '__all__'
        many = True