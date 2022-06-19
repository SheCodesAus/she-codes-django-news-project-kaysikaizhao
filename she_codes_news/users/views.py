from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View, generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class DisplayProfile(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'

class AuthorsView(generic.ListView):
    template_name = 'users/authors.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = CustomUser.objects.all()
        return context

