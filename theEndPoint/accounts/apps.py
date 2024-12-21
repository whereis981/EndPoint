from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theEndPoint.accounts'

    def ready(self):
        import theEndPoint.accounts.signals
