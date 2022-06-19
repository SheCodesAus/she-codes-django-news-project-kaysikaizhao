from django.urls import path, re_path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # path('view-story/<int:author_id>', views.StoriesByAuthorView.as_view(), name='storiesByAuthor')
    re_path(r'^view_story/(?P<author>\d+)$', views.StoriesByAuthorView.as_view(), name='storiesByAuthor'),
]


