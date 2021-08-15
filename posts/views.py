from django.shortcuts import render
from .models import Post

def post_view(request, *args, **kwargs):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, template_name='home.html', context=context)