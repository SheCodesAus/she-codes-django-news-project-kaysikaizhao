from django.urls import path
from .views import CreateAccountView, DisplayProfile

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name='createAccount'),
    path('profile/<int:pk>', DisplayProfile.as_view(), name="profile")
]