# D:\Trablho\Siteeletromaciel\custom_backend.py
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures as MySqlDatabaseFeatures

class DatabaseFeatures(MySqlDatabaseFeatures):
    # 🎯 Força o Django a NUNCA usar RETURNING em nenhuma operação de insert
    can_return_rows_from_insert = False
    can_return_ids_from_insert = False

class DatabaseWrapper(MySQLDatabaseWrapper):
    features_class = DatabaseFeatures