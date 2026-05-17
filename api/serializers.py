from rest_framework import serializers
from .models import Produtos, Usuarios

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        # Aqui listamos os campos essenciais que mapeamos no phpMyAdmin!
        fields = ['id', 'codigo', 'descricao', 'estoque', 'minimo', 'grupodesc', 'fabricantedesc']

# --- Novo Serializer para os Usuários ---
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        # Vamos expor os campos necessários para o login e nível de acesso
        fields = ['codigo', 'usuario', 'login', 'ativo','permissao']