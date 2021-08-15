from django.urls import path
from .views import register_view
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]