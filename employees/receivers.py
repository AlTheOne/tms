from django.db.models.signals import pre_save
from django.dispatch import receiver

from employees.models import Notification
from tasks.models import Task


@receiver(pre_save, sender=Task)
def create_notification(sender, instance, **kwargs):
    """
    Формирование оповещения в случае изменения задачи.
    """

    if not instance._state.adding:
        old_instance = sender.objects.get(pk=instance.pk)

        has_update = False
        change_executor = False

        checked_fields = (
            'priority', 'project', 'description', 'time_estimate',
            'time_spent', 'executor',
        )
        for field in checked_fields:
            if getattr(old_instance, field) != getattr(instance, field):
                has_update = True
                if field == 'executor':
                    change_executor = True

        # Есть обновления -> оповещаем сотрудника
        if has_update and old_instance.executor:
            Notification.objects.create(
                employee=old_instance.executor,
                task=old_instance,
            )

        # Оповещаем нового исполнителя
        if change_executor and instance.executor:
            Notification.objects.create(
                employee=instance.executor,
                task=old_instance,
            )
