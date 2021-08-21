from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Post

def post_view(request, *args, **kwargs):
    context = {
        'posts': Post.objects.all().order_by('-date_posted'),
    }
    return render(request, template_name='home.html', context=context)

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if not query:
            return Post.objects.none()
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        if posts.exists():
            # print(posts)
            return posts
        else:
            return Post.objects.none()