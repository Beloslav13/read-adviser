from django.db import models

from server.apps.common.models import AbstractBaseModel


class Link(AbstractBaseModel):
    """Ссылка на источник информации"""

    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        blank=True,
        null=True
    )

    url = models.URLField(
        verbose_name='Ссылка'
    )
    owner = models.ForeignKey(
        verbose_name='Владелец',
        to='user.User',
        on_delete=models.CASCADE,
        related_name='links'
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to='Category',
        on_delete=models.CASCADE,
        related_name='links'
    )

    class Meta(AbstractBaseModel.Meta):
        abstract = False
        verbose_name = "Ссылка"
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.entity_name

    @property
    def entity_name(self):
        tmp = f'{self.name if self.name else ""}: {self.url}'
        return tmp
