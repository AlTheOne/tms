from django.db import models


class Project(models.Model):

    title = models.CharField(
        verbose_name='название',
        max_length=400,
        unique=True,
    )

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def __str__(self):
        return self.title
