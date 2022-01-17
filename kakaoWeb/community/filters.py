import django_filters
from .models import *

class CommunityFilter(django_filters.FilterSet):

    class Meta:
        model = Community
        fields = [
            'category',
        ]