from django.apps import AppConfig


class ContatoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Contato'
    
    def ready(self):
        import Contato.signals
