from django.apps import AppConfig


class DennisivySignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dennisivy_signals'

    def ready(self):
        import dennisivy_signals.signals
