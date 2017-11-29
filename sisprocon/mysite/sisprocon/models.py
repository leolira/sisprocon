from django.db import models

ENUM_TIPOSDEPRODUTO = (
    ('1', 'Alimentos'),
    ('2', 'Limpeza'),
    ('3', 'Frios'),
    ('4', 'Escritorio'),
)

ENUM_RAMOS = (
    ('1', 'Supermercados'),
    ('2', 'Textil'),
    ('3', 'Postos de Combustiveis'),
    ('4', 'Acougues'),
)

ENUM_TIPOFISC = (
    ('1', 'Precos'),
    ('2', 'Cumprimento de Lei'),
)

ENUM_PARECER = (
    ('0', 'Regular'),
    ('1', 'Irregular'),
)


class Pesquisas(models.Model):
    data = models.DateField(null=True, blank=True)
    descricaoPesquisa = models.CharField(max_length=250)
    responsavel = models.CharField(max_length=50)
    def __str__(self):
        return self.descricaoPesquisa

class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    descricaoProduto = models.CharField(max_length=250)
    tipoProduto = models.CharField(max_length=20, choices=ENUM_TIPOSDEPRODUTO)
    categoriaProduto = models.CharField(max_length=50)
    def __str__(self):
        return self.descricaoProduto

class OrgaosFiscalizadores(models.Model):
    nomeOrgao = models.CharField(max_length=50) 
    email = models.CharField(max_length=50)
    nomeContato = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    diretor = models.CharField(max_length=50)
    telefoneContato = models.CharField(max_length=15)
    endereco = models.CharField(max_length=150)
    def __str__(self):
        return self.nomeOrgao

class Empresas(models.Model):
    razaoSocial = models.CharField(max_length=50)
    nomeFantasia = models.CharField(max_length=50)
    ramo = models.CharField(max_length=20, choices=ENUM_RAMOS)
    cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    def __str__(self):
        return self.razaoSocial
    
class OrgaoDePesquisa(models.Model):
    idOrgao = models.ForeignKey(OrgaosFiscalizadores)
    idPesquisa = models.ForeignKey(Pesquisas)
    def __str__(self):
        return self.idOrgao

class ProdutosDasEmpresas(models.Model):
    idEmpresa = models.ForeignKey(Empresas)
    idProduto = models.ForeignKey(Produtos) 
    def __str__(self):
        return self.idEmpresa

class Precos(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    idProdutoEmpresa = models.ForeignKey(ProdutosDasEmpresas, default=0)
    idPesquisa = models.ForeignKey(Pesquisas, default=0)
    def __str__(self):
        return self.preco

class Fiscalizacoes(models.Model):
    data = models.DateField(null=True, blank=True)
    descricaoFiscalizacao = models.CharField(max_length=250)
    parecer = models.CharField(max_length=20, choices=ENUM_PARECER)
    observacao = models.CharField(max_length=250)
    tipoFiscalizacao = models.CharField(max_length=20, choices=ENUM_TIPOFISC)
    idOrgao = models.ForeignKey(OrgaosFiscalizadores)
    idEmpresa = models.ForeignKey(Empresas)
    def __str__(self):
        return self.descricaoFiscalizacao

