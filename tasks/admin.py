from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        'id', '__str__', 'project', 'priority', 'status', 'date_updated',
        'date_created',
    )
    list_display_links = ('id', '__str__')

    list_filter = ('priority', 'status')

    readonly_fields = ('date_updated', 'date_created')
    save_on_top = True
