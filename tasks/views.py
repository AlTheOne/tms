from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Value, CharField
from django.views.generic import (
    ListView, DetailView, UpdateView, CreateView, FormView,
)

from .forms import TaskForm, ReportForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    queryset = Task.objects.all()
    paginate_by = 10

    def get_queryset(self):
        return self.queryset.select_related(
            'project',
        ).only(
            'project__title',
            'description',
            'date_updated',
            'date_created',
        )


class SearchTaskView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    queryset = Task.objects.all()
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        return self.queryset.filter(
            description__icontains=query,
        ).select_related(
            'project',
        ).only(
            'project__title',
            'description',
            'date_updated',
            'date_created',
        )


class TaskCreateView(LoginRequiredMixin, CreateView):

    login_url = '/login/'
    template_name = 'tasks/task_form_create.html'
    form_class = TaskForm

    def form_valid(self, form):

        # Указываем автора
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):

    login_url = '/login/'
    queryset = Task.objects.all()

    def get_queryset(self):
        return self.queryset.select_related(
            'project',
            'executor',
            'created_by',
        ).only(
            'priority',
            'status',
            'project__title',
            'description',
            'time_estimate',
            'time_spent',
            'executor__name',
            'created_by__username',
            'date_updated',
            'date_created',
        )


class TaskUpdateView(LoginRequiredMixin, UpdateView):

    login_url = '/login/'
    queryset = Task.objects.exclude(status=0)
    template_name = 'tasks/task_form_update.html'
    form_class = TaskForm


class ReportView(LoginRequiredMixin, FormView):

    login_url = '/login/'
    template_name = 'tasks/task_report.html'
    form_class = ReportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET:
            form = self.form_class(self.request.GET)
            context['form'] = form
            if form.is_valid():
                context['object_list'] = self.get_report_queryset(form)

        return context

    def get_report_queryset(self, form):
        """
        Формирование QuerySet'а для отчёта.
        """
        queryset = Task.objects.all()

        project = form.cleaned_data.get('project')
        queryset = queryset.filter(project=project)

        start_date = form.cleaned_data.get('start_date')
        if start_date:
            queryset = queryset.filter(date_updated__gte=start_date)

        end_date = form.cleaned_data.get('end_date')
        if end_date:
            queryset = queryset.filter(date_updated__lte=end_date)

        subquery = Task.objects.filter(
            project=project,
        ).aggregate(
            total=Sum('time_spent'),
        )
        queryset = queryset.annotate(
            total=Value(subquery['total'], CharField()))

        return queryset.select_related(
            'project',
        ).only(
            'project__title',
            'description',
            'date_updated',
            'date_created',
        )
