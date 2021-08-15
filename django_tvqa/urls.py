"""django_tvqa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from users.views import register_view
from django.contrib.auth import views as auth_views
from posts.views import post_view
from pmods.views import pmod_bom_create_view, pmod_bom_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_view, name='index'),
    path('home/', post_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('pmod_bom_create/', pmod_bom_create_view, name='pmod_bom_create'),
    path('pmod_bom_list/', pmod_bom_list_view, name='pmod_bom_list'),
]
