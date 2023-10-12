from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=12)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=12)

    def __str__(self):
        return self.nome
    
class funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=12)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=12)
    salario = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nome
    
class categoriaServico(models.Model):
    nome = models.CharField(max_length=100)
    valorMaoDeObra = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nome
    
class produto(models.Model):
    nome = models.CharField(max_length=50)
    QuantEstoque = models.IntegerField()
    codigoFabricante = models.CharField(max_length=100)
    nomeFabricante = models.CharField(max_length=100)
    valorCompra = models.DecimalField(max_digits=10,decimal_places=2)
    valorVenda = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nome
    
class automovel(models.Model):
    CATEGORIA_AUTOMOVEL = [
        ("CARRO","CARRO"),
        ("MOTO","MOTO"),
        ("CAMINHÃO","CAMINHÃO"),
    ]

    categoria = models.CharField(max_length=100, choices=CATEGORIA_AUTOMOVEL)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=4)
    clienteFK = models.ForeignKey(cliente, related_name='automovelCliente', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.marca + '-' + self.modelo
    
class manutencao(models.Model):
    automovelFK = models.ForeignKey(automovel, related_name='manutençãoAutomovel', on_delete=models.CASCADE)
    funcionarioFK = models.ForeignKey(funcionario, related_name='manutençãoFuncionario', on_delete=models.CASCADE)
    valorTotal = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)

    def __str__(self):
        return self.automovelFK.modelo
    
class manutencao_categoria(models.Model):
    manutencaoFK = models.ForeignKey(manutencao, related_name='manutençãoCategoria', on_delete=models.CASCADE)
    categoriaFK = models.ForeignKey(categoriaServico, related_name='categoriaManutenção', on_delete=models.CASCADE)

    def __str__(self):
        return self.manutencaoFK.automovelFK.modelo + '-' + self.categoriaFK.nome
    
class manutencao_produto(models.Model):
    manutencaoFK = models.ForeignKey(manutencao, related_name='manutençãoProduto', on_delete=models.CASCADE)
    produtoFK = models.ForeignKey(produto, related_name='produtoManutenção', on_delete=models.CASCADE)

    def __str__(self):
        return self.manutencaoFK.automovelFK.modelo + '-' + self.produtoFK.nome
    
class pagamento(models.Model):
    CATEGORIA_PAGAMENTO = [
        ("PIX","PIX"),
        ("BOLETO","BOLETO"),
        ("CC","CARTÃO DE CREDITO"),
        ("CD","CARTÃO DE DEBITO"),
    ]

    STATUS = [
        ("P","PENDENTE"),
        ("A","APROVADO"),
        ("C","CANCELADO"),
    ]

    categoria = models.CharField(max_length=100, choices=CATEGORIA_PAGAMENTO)
    descricao = models.CharField(max_length=100)
    manutencaoFK = models.ForeignKey(manutencao, related_name='pagamentoManutenção', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS)
    valorDesconto = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)
    valorFinal = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)

    def __str__(self):
        return self.descricao

class postoTrabalho(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class posto_funcionario(models.Model):
    postoFK =  models.ForeignKey(postoTrabalho, related_name='posto', on_delete=models.CASCADE)
    funcionarioFK = models.ForeignKey(funcionario, related_name='postoFuncionario', on_delete=models.CASCADE)

    def __str__(self):
        return self.postoFK.descricao + '-' + self.funcionarioFK.nome
    
class reserva(models.Model):
    clienteFK = models.ForeignKey(cliente, related_name='reservaCliente', on_delete=models.CASCADE)
    postoFK = models.ForeignKey(postoTrabalho, related_name='reservaPosto', on_delete=models.CASCADE)
    manutencaoFK = models.ForeignKey(manutencao, related_name='reservaManutenção', on_delete=models.CASCADE,null=True, blank=True)
    dia = models.DateField()
    comentario = models.CharField(max_length=400, null=True, blank=True)
    nota = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    dataCriacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.clienteFK.nome + '-' + str(self.dia)
    
class disponibilidade(models.Model):
    postoFK = models.ForeignKey(postoTrabalho, related_name='disponibilidadePosto', on_delete=models.CASCADE)
    reservaFK = models.ForeignKey(reserva, related_name='disponibilidadeReserva', on_delete=models.CASCADE, null=True, blank=True)
    dia = models.DateField()

    def __str__(self):
        return self.postoFK.descricao + '-' + str(self.dia)

