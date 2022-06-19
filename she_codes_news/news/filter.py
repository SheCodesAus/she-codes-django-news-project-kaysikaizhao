import django_filters
from .models import NewsStory

class AuthorFilter(django_filters.FilterSet):

    class Meta:
        model = NewsStory
        fields = ['author']