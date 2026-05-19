from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # 🎯 Pulo do gato: Desativamos o RETURNING direto na memória assim que o app liga!
        try:
            from django.db import connections
            from django.db.utils import ConnectionHandler
            
            # Aplicamos a trava para a conexão padrão do banco
            connections['default'].features.can_return_rows_from_insert = False
            connections['default'].features.can_return_ids_from_insert = False
            
            print("🚀 [Eletromaciel] Bloqueio do RETURNING injetado com sucesso na memória!")
        except Exception as e:
            print(f"⚠️ Erro ao injetar trava do banco: {e}")