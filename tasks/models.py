from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from employees.models import Employee


class Task(models.Model):

    PRIORITY_CHOICES = (
        (0, 'Высокий'),
        (1, 'Средний'),
        (2, 'Низкий'),
    )
    STATUS_CHOICES = (
        (0, 'Реализовано'),
        (1, 'Новая'),
        (2, 'В процессе'),
    )

    priority = models.IntegerField(
        verbose_name='приоритет',
        choices=PRIORITY_CHOICES,
        default=1,
    )
    status = models.IntegerField(
        verbose_name='статус',
        choices=STATUS_CHOICES,
        default=1,
    )

    project = models.ForeignKey(
        verbose_name='проект',
        to='projects.Project',
        on_delete=models.CASCADE,
    )

    description = models.TextField(
        verbose_name='описание',
    )

    time_estimate = models.DurationField(
        verbose_name='оценка времени на реализацию',
    )
    time_spent = models.DurationField(
        verbose_name='затраченное время на реализацию',
        null=True,
        blank=True,
    )

    executor = models.ForeignKey(
        verbose_name='исполнитель',
        to=Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        verbose_name='автор',
        to=User,
        on_delete=models.SET_NULL,
        null=True,
    )

    date_updated = models.DateTimeField(
        verbose_name='обновлено',
        auto_now_add=False,
        auto_now=True,
    )
    date_created = models.DateTimeField(
        verbose_name='создано',
        auto_now_add=True,
        auto_now=False,
    )

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ('-date_created',)

    def __str__(self):
        return 'Задача #{}'.format(self.pk)

    def get_absolute_url(self):
        return reverse('task-detail', args=(self.pk,))
