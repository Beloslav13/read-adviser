from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_default_category(sender, **kwargs):
    from server.apps.adviser.models.category import CategoryChoices
    from server.apps.adviser.models import Category

    cat_create = []
    for cat in CategoryChoices.choices:
        if not Category.objects.filter(type=cat[0]).exists():
            cat_create.append(Category(type=cat[0]))

    Category.objects.bulk_create(cat_create)

class AdviserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.adviser'
    label = 'adviser'
    verbose_name = 'Советник'

    def ready(self):
        from server import signals
        post_migrate.connect(create_default_category, sender=self)