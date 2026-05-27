from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # <-- Garanta esta importação
from rest_framework.authentication import TokenAuthentication  # <-- Garanta esta importação
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import connection
from .models import Produtos, Usuarios
from .serializers import ProdutosSerializer, UsuariosSerializer, CadastroProdutoSerializer
from rest_framework.parsers import MultiPartParser, FormParser


#1. CATÁLOGO PROTEGIDO
class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    permission_classes = [IsAuthenticated]  # <-- Adicione esta linha para exigir autenticação
    authentication_classes = [TokenAuthentication]  # <-- Adicione esta linha para usar autenticação baseada em token
# 🎯 BY-PASS TOTAL NO ORM DO DJANGO PARA EVITAR O RETURNING
    def perform_create(self, serializer):
        # Coletamos os dados limpos e validados que vieram do WordPress
        dados = serializer.validated_data

        # 1. Captura quem está logado fazendo a requisição (enviado pelo Token)
        # Se por algum motivo o token não identificar o nome, ele grava como 'WordPress_API'
        usuario_responsavel = self.request.user.username if self.request.user.is_authenticated else 'WordPress_API'
        
        # Escrevemos a query clássica na força bruta. Sem RETURNING!
        # Nota: Ajuste as colunas e os nomes se no banco estiver em maiúsculo (ex: ID, CODIGO)
        query_produto = """
            INSERT INTO produtos (codigo, descricao, estoque, minimo, grupodesc, fabricantedesc)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        params_produto = [
            dados.get('codigo'),
            dados.get('descricao'),
            dados.get('estoque', 0),
            dados.get('minimo', 0),
            dados.get('grupodesc', ''),
            dados.get('fabricantedesc', '')
        ]

        # 3. Query de Auditoria (Gravação do rastro)
        query_log = """
            INSERT INTO logs_auditoria (usuario, acao, detalhes)
            VALUES (%s, %s, %s)
        """
        params_log = [
            usuario_responsavel,
            'CRIAR',
            f"Cadastrou o produto {dados.get('codigo')} - {dados.get('descricao')}"
        ]
        
        # Executamos direto no cursor do MySQLdb
        with connection.cursor() as cursor:
            cursor.execute(query_produto, params_produto)
            cursor.execute(query_log, params_log)

# 2. CRUD DE USUÁRIOS
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

# 3. ENDPOINT EXCLUSIVO PARA LOGIN INTEGRADO (Novo)
class LoginIntegradoView(APIView):
    authentication_classes = []  # Liberado publicamente para tentativas de login
    permission_classes = []

    def post(self, request):
        username_enviado = request.data.get('usuario')
        senha_enviada = request.data.get('senha')

        # 🎯 O Django agora valida TODO MUNDO em uma única linha, usando criptografia!
        user = authenticate(username=username_enviado, password=senha_enviada)

        if user is not None:
            # Pega ou gera o Token de segurança amarrado ao usuário
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({
                'mensagem': 'Login realizado com sucesso!',
                'token': token.key,
                'usuario': user.username,
                'permissao': 'admin' if user.is_superuser else 'user'
            }, status=status.HTTP_200_OK)

        # Se o authenticate retornar None, significa que o usuário não existe ou a senha errou
        return Response({'erro': 'Usuário ou senha incorretos.'}, status=status.HTTP_401_UNAUTHORIZED)
class CadastroProdutoView(APIView):
    # 🔒 Segurança: Apenas funcionários logados (como o LUCIANO) podem cadastrar
    permission_classes = [IsAuthenticated] 
    parser_classes = [MultiPartParser, FormParser]  # Permite receber imagens do formulário

    def post(self, request):
        serializer = CadastroProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'mensagem': 'Produto cadastrado com sucesso!',
                'dados': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)