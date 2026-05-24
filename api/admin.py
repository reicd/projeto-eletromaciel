from django.contrib import admin
from .models import Produtos # Garanta que Produtos esteja mapeado no seu models.py
from .models import Auditoria  # Certifique-se de que o nome está exatamente como no seu models.py

# 📊 Customização visual da tabela de produtos no Admin
@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'estoque', 'minimo', 'grupodesc', 'fabricantedesc')
    search_fields = ('codigo', 'descricao')
    list_filter = ('grupodesc', 'fabricantedesc')

# 🕵️‍♂️ Criando a visualização dos Logs de Auditoria no Admin
# Como criamos a tabela logs_auditoria direto no phpMyAdmin, podemos mapear um Model rápido para ela ou apenas visualizá-la.
# Register your models here.
@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    # Escolha as colunas que você quer ver listadas na tela do painel:
    list_display = ('id', 'operacao', 'usuario', 'maquina', 'ip', 'data', 'hora')
    
    # Adiciona filtros automáticos na barra lateral direita para facilitar a investigação:
    list_filter = ('data', 'usuario', 'operacao')
    
    # Adiciona uma barra de pesquisa para buscar por termos específicos (ex: buscar um IP ou operação):
    search_fields = ('operacao', 'usuario', 'ip', 'tsql') 