import django_filters
from .models import College_Info

class DetailFilter(django_filters.FilterSet):
    class Meta:
        model = College_Info
        fields = '__all__'