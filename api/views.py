from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # <-- Garanta esta importação
from rest_framework.authentication import TokenAuthentication  # <-- Garanta esta importação

from .models import Produtos, Usuarios
from .serializers import ProdutosSerializer, UsuariosSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    permission_classes = [IsAuthenticated]  # <-- Adicione esta linha para exigir autenticação
    authentication_classes = [TokenAuthentication]  # <-- Adicione esta linha para usar autenticação baseada em token
# --- Nova ViewSet para os Usuários ---
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
