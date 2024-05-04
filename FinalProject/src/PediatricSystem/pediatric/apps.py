from django.apps import AppConfig


class PediatricConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pediatric"

    def ready(self):
        import pediatric.signals
