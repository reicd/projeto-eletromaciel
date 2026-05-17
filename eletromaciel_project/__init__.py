from django.db.backends.base.base import BaseDatabaseWrapper

# Sobrescreve a checagem de versão do Django para aceitar seu MariaDB atual
BaseDatabaseWrapper.check_database_version_supported = lambda self: None