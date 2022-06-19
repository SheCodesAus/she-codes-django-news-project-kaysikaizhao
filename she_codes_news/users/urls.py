from django.urls import path
from .views import CreateAccountView, DisplayProfile, AuthorsView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name='createAccount'),
    path('profile/<int:pk>', DisplayProfile.as_view(), name="profile"),    
    path('authors', AuthorsView.as_view(), name="authors")
]