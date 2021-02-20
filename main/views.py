from django.shortcuts import render

from .models import Post, Comment


def index(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'index.html', context)
