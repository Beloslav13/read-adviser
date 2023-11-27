from django.contrib.auth.models import AbstractUser
from django.db import models

from server.apps.common.models import AbstractBaseModel

class User(AbstractBaseModel, AbstractUser):

    email = models.EmailField(
        'Адрес электронной почты',
        unique=True,
    )
    middle_name = models.CharField(
        'Отчество',
        max_length=55,
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'

    @property
    def full_name(self) -> str:
        """ФИО пользователя."""

        names_elements = (self.last_name, self.first_name, self.middle_name)
        if not any(names_elements):
            return ''
        return ' '.join(filter(None, names_elements)).strip()

    def get_links(self):
        # Link.objects.filter(owner=self)
        return self.get_relations('link')