from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input the title here'}),
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
            'content': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input the title here'})
        }

