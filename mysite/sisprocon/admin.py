from django.contrib import admin

from .models import Pesquisas, Produtos, OrgaosFiscalizadores, Empresas, OrgaoDePesquisa, ProdutosDasEmpresas, Precos, Fiscalizacoes

admin.site.register(Pesquisas)
admin.site.register(Produtos)
admin.site.register(OrgaosFiscalizadores)
admin.site.register(Empresas)
admin.site.register(OrgaoDePesquisa)
admin.site.register(ProdutosDasEmpresas)
admin.site.register(Precos)
admin.site.register(Fiscalizacoes)
