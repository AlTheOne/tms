from django import forms

from projects.models import Project
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = (
            'project', 'priority', 'status', 'description', 'time_estimate',
            'time_spent', 'executor',
        )


class ReportForm(forms.Form):

    project = forms.ModelChoiceField(
        label='Проект',
        queryset=Project.objects.all(),
    )

    start_date = forms.DateTimeField(
        label='Начальная дата',
        required=False,
    )
    end_date = forms.DateTimeField(
        label='Конечная дата',
        required=False,
    )
