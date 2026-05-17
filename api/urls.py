from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutosViewSet, UsuariosViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutosViewSet)
# --- Registrando a nova ViewSet para os Usuários ---
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]