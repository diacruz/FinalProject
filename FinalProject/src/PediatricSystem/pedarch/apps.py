from django.apps import AppConfig

class PedarchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pedarch'

    def ready(self):
        import pediatric.signals  # Import signals here if you have any
