import django_filters

from .models import *

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['name','color']