import django_filters
from .models import *

class MachineFilter(django_filters.FilterSet):
    class Meta:
        model = Machine
        fields = ['year', 'model', 'model__series']