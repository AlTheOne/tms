from django.urls import path

from .views import (
    TaskListView, TaskDetailView, TaskUpdateView, TaskCreateView,
    SearchTaskView, ReportView,
)

urlpatterns = [
    path(
        '',
        TaskListView.as_view(),
        name='task-list',
    ),
    path(
        'add/',
        TaskCreateView.as_view(),
        name='task-add',
    ),
    path(
        'search/',
        SearchTaskView.as_view(),
        name='task-search_result',
    ),
    path(
        '<int:pk>/',
        TaskDetailView.as_view(),
        name='task-detail',
    ),
    path(
        '<int:pk>/edit/',
        TaskUpdateView.as_view(),
        name='task-edit',
    ),
    path(
        'report/',
        ReportView.as_view(),
        name='task-report',
    ),
]
