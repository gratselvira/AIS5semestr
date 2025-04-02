from django.apps import AppConfig

# информацию о приложении, которое может быть полезной при конфигурации проекта.

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
