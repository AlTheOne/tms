from django.contrib import admin

from .models import Employee, Notification


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'project')
    list_display_links = ('id', 'name')

    list_filter = ('project',)
    search_fields = ('name', 'email')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = ('id', 'task', 'employee', 'is_check', 'date_created')
    list_display_links = ('id', 'task')

    list_filter = ('is_check',)
