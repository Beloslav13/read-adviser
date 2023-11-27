from django.apps import AppConfig


class AdviserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.adviser'
    label = 'adviser'
    verbose_name = 'Советник'
