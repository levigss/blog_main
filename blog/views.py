from django.shortcuts import render, get_object_or_404 # Estaba incompleto
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})