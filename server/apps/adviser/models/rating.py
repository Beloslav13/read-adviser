from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CheckConstraint, UniqueConstraint, Q

from server.apps.adviser.models import Link
from server.apps.common import AbstractBaseModel


class Rating(AbstractBaseModel):
    rate = models.FloatField(
        verbose_name='Рейтинг',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )

    link = models.ForeignKey(
        verbose_name='Ссылка',
        to=Link,
        on_delete=models.CASCADE,
        related_name='rating'
    )

    owner = models.ForeignKey(
        verbose_name='Пользователь',
        to='user.User',
        on_delete=models.CASCADE,
        related_name='rating'
    )

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        constraints = [
            CheckConstraint(check=Q(rate__range=(0, 5)), name='valid_rate'),
            UniqueConstraint(fields=['owner', 'link'], name='rating_once')
        ]

    def __str__(self):
        return self.entity_name

    @property
    def entity_name(self):
        return f'Рейтинг: {self.rate}, ссылка: {self.link_id}'
