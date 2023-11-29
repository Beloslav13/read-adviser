from django.db import models

from server.apps.common.models import AbstractBaseModel


class CategoryChoices(models.IntegerChoices):
    UNKNOWN = 10, 'Не определено'
    VIDEO = 20, 'Видео'
    ARTICLE = 30, 'Статья'
    NEWS = 40, 'Новость'


class Category(AbstractBaseModel):

    type = models.IntegerField(
        verbose_name='Категория',
        choices=CategoryChoices.choices,
        default=CategoryChoices.UNKNOWN,
        unique=True,
        db_index=True
    )

    class Meta(AbstractBaseModel.Meta):
        abstract = False
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.entity_name

    @property
    def entity_name(self):
        return f'{self.get_type_display()}'

    def get_links(self):
        return self.get_relations('link')
