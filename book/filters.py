import django_filters
from .models import Service

class ServiceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['title']