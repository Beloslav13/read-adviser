from django.db import models

from server.apps.common.models import AbstractBaseModel

class Category(AbstractBaseModel):

    class CategoryChoices(models.IntegerChoices):
        UNKNOWN_CATEGORY = 0, 'Не определено'
        VIDEO_CATEGORY = 10, 'Видео'
        ARTICLE_CATEGORY = 20, 'Статья'
        NEWS_CATEGORY = 30, 'Новость'

    class Meta(AbstractBaseModel.Meta):
        abstract = False
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    type = models.IntegerField(
        verbose_name='Категория',
        choices=CategoryChoices.choices,
        default=CategoryChoices.UNKNOWN_CATEGORY,
        unique=True,
        db_index=True
    )

    def __str__(self):
        return self.entity_name

    @property
    def entity_name(self):
        return f'{self.get_type_display()}'

    def get_links(self):
        return self.get_relations('link')
