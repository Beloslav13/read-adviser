from django.apps import AppConfig
from django.db.models.signals import post_migrate

# todo: for dev, after delete...
def create_superuser(sender, **kwargs):
    from server.apps.user.models import User
    username = 'root'
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, password='root')


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.user'
    label = 'user'
    verbose_name = 'Пользователь'

    def ready(self):
        post_migrate.connect(create_superuser, sender=self)