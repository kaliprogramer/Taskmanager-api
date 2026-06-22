import django_filters
from .models import Task
class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    completed = django_filters.BooleanFilter()

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']