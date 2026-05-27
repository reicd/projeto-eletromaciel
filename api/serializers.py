from rest_framework import serializers
from .models import Produtos, Usuarios

# ====================================================
# 1. LISTAGEM DE PRODUTOS (Para o catálogo)
# ====================================================
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        # Campos essenciais mapeados no phpMyAdmin
        fields = ['id', 'codigo', 'descricao', 'estoque', 'minimo', 'grupodesc', 'fabricantedesc','nova_imagem', 'descricao_acessivel'
                  ]


# ====================================================
# 2. LISTAGEM DE USUÁRIOS (Controle antigo)
# ====================================================
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        # Campos necessários para verificar dados herdados
        fields = ['codigo', 'usuario', 'login', 'ativo', 'permissao']


# ====================================================
# 3. CADASTRO DE PRODUTOS (Com Acessibilidade PcD)
# ====================================================
class CadastroProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        # Campos recebidos pelo formulário do WordPress
        fields = [
            'codigo', 'descricao', 'estoque', 'venda', 
            'nova_imagem', 'descricao_acessivel'
        ]

    def create(self, validated_data):
        # Injeta os valores padrão que o banco antigo exige
        validated_data['ativo'] = 1
        validated_data['empresa'] = 1
        validated_data['situacao'] = 1
        validated_data['unidade'] = 'UN'
        
        return super().create(validated_data)
