from django.db import models


class Employee(models.Model):

    name = models.CharField(
        verbose_name='имя',
        max_length=256,
    )

    project = models.ForeignKey(
        verbose_name='проект',
        to='projects.Project',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        verbose_name='почта',
        unique=True,
    )

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

    def __str__(self):
        return self.name


class Notification(models.Model):

    employee = models.ForeignKey(
        verbose_name='сотрудник',
        to='employees.Employee',
        on_delete=models.CASCADE,
    )

    task = models.ForeignKey(
        verbose_name='задача',
        to='tasks.Task',
        on_delete=models.CASCADE,
    )

    is_check = models.BooleanField(
        verbose_name='просмотрено',
        default=False,
    )

    date_created = models.DateTimeField(
        verbose_name='создано',
        auto_now_add=True,
        auto_now=False,
    )

    class Meta:
        verbose_name = 'оповещение'
        verbose_name_plural = 'оповещения'

    def __str__(self):
        return 'Оповещение #{}'.format(self.pk)

