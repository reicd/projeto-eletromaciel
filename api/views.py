from rest_framework import viewsets
from .models import Produtos, Usuarios
from .serializers import ProdutosSerializer, UsuariosSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

# --- Nova ViewSet para os Usuários ---
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
