from .views import post_view, SearchResultsView
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', post_view, name='index'),
    path('home/', post_view, name='home'),
]