from django.db import models
from django.db.models import Avg

from server.apps.common.models import AbstractBaseModel


class LinkChoices(models.IntegerChoices):
    UNKNOWN = 10, 'Не определено'
    APP = 20, 'Приложение'
    TELEGRAM = 30, 'Телеграм'


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

    source = models.SmallIntegerField(
        verbose_name='Источник',
        choices=LinkChoices.choices,
        default=LinkChoices.UNKNOWN,
        db_index=True
    )

    is_read = models.BooleanField(
        verbose_name='Прочитано',
        default=False
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

    @property
    def average_rating(self):
        return self.rating.all().aggregate(Avg('rate'))['rate__avg']
