from django.contrib.contenttypes.models import ContentType
from django.db import models


class AbstractBaseModel(models.Model):
    """Базовая модель."""

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        abstract = True
        ordering = ['id']


    @property
    def entity_name(self):
        return f'{self.__class__.__name__}#{self.pk}'

    @property
    def entity_model(self):
        return f'{self.__class__.__name__}'.lower()

    def get_relations(self, entity_model: str):
        try:
            _model = ContentType.objects.get(app_label='adviser', model=entity_model)
        except ContentType.DoesNotExist:
            return None
        else:
            lookup_field = self.entity_model if self.entity_model != 'user' else 'owner'
            return _model.model_class().objects.filter(**{lookup_field: self})