from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutosViewSet, UsuariosViewSet, LoginIntegradoView

router = DefaultRouter()
router.register(r'produtos', ProdutosViewSet)
# --- Registrando a nova ViewSet para os Usuários ---
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    # 🎯 Nova rota para o formulário de login (DEVE VIR ANTES DO INCLUDE)
    path('login-integrado/', LoginIntegradoView.as_view(), name='login_integrado'),
    
    # Rotas automáticas do roteador (produtos e usuarios)
    path('', include(router.urls)),
]