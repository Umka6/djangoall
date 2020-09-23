from django.shortcuts import render
from .models import Post
def posts_list(request):
    posts = Post.objects.all()
    n = 'oleg'
    return render(request, 'blog/index.html', context={'posts': posts})
# Create your views here.
