from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404

from .models import Post, Like


def index(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'index.html', context)


def detail(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        raise Http404('Post Not Found!')

    comments = p.comment_set.all()

    context = {
        'post': p,
        'comments': comments
    }
    return render(request, 'detail.html', context)


def leave_comment(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        raise Http404('Post Not Found!')

    username = request.user.username
    p.comment_set.create(user=username, text=request.POST.get('text'))

    return redirect(reverse('detail', args=(p.id,)))


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()

    return redirect('index')
