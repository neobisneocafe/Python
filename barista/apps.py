from django.apps import AppConfig


class LowbarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barista'

    def ready(self):
        import barista.signals
