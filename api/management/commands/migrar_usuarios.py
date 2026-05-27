from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Usuarios  # Certifique-se de que o nome do modelo está correto

class Command(BaseCommand):
    help = 'Migra de forma definitiva os utilizadores da tabela antiga para a auth_user do Django'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('🚀 A iniciar a migração de utilizadores...'))
        
        # Procura todos os utilizadores na tabela antiga
        usuarios_antigos = Usuarios.objects.all()
        contador_sucesso = 0

        for antigo in usuarios_antigos:
            # 🎯 Mudamos para minúsculas: antigo.usuario e antigo.login
            username_final = (antigo.usuario or antigo.login)
            if username_final:
                username_final = username_final.strip()
            
            if not username_final:
                self.stdout.write(self.style.ERROR('⚠️ Ignorado: Utilizador sem nome ou login preenchido.'))
                continue

            # Verifica se o utilizador já foi migrado para não duplicar
            if User.objects.filter(username=username_final).exists():
                self.stdout.write(self.style.NOTICE(f'ℹ️ O utilizador "{username_final}" já existe no Django. A saltar...'))
                continue

            try:
                # 🎯 Mudamos para minúsculo: antigo.senha
                senha_limpa = antigo.senha.strip() if antigo.senha else 'Mudar123!'
                
                # Cria o usuário com o hash de segurança nativo
                novo_usuario = User.objects.create_user(
                    username=username_final,
                    password=senha_limpa
                )
                
                # 🎯 Mudamos para minúsculo: antigo.permissao
                # Mantivemos a regra para dar privilégios caso encontre o 'MARCELO'
                if antigo.permissao and ('admin' in antigo.permissao.lower() or username_final.upper() == 'MARCELO'):
                    novo_usuario.is_staff = True
                    novo_usuario.is_superuser = True
                    novo_usuario.save()

                self.stdout.write(self.style.SUCCESS(f'✅ Utilizador "{username_final}" migrado com sucesso!'))
                contador_sucesso += 1

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Erro ao migrar "{username_final}": {str(e)}'))

        self.stdout.write(self.style.SUCCESS(f'🎉 Maravilha! {contador_sucesso} utilizadores foram integrados oficialmente!'))