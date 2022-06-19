from django.views import generic
from django.urls import reverse_lazy

# from she_codes_news.news.filter import SnippetFilter
from .models import NewsStory
from .forms import StoryForm
from .filter import AuthorFilter

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewStorybyAuthorView(generic.ListView):
    model = NewsStory
    template_name = 'news/author.html'

    # def get_author_name(self, **kwargs, pk):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['author'] = AuthorFilter(self.request.GET, queryset=self.get_queryset())
        # context['author'] = NewsStory.objects.filter(author=username)
        # return context

        def get_queryset(self):
            return NewsStory.objects.filter(author = NewsStory.username)

class StoriesByAuthorView(generic.ListView):
    template_name = 'news/storiesByAuthor.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories_by_author'] = NewsStory.objects.all().filter(author=self.kwargs['author'])
        return context