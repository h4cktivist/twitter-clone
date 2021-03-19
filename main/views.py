from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.utils import timezone
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Post, Like
from .forms import PostCreationForm


def index(request):
    if request.method == 'POST':
        try:
            form = PostCreationForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.date = timezone.now()
                post.save()
        except ValueError:
            return redirect('login')

    posts = Post.objects.order_by('-date')
    form = PostCreationForm()

    context = {'posts': posts, 'form': form}
    return render(request, 'index.html', context)


def search(request):
    search_data = request.POST.get('input_search')
    posts = Post.objects.filter(text__contains=search_data)

    context = {'posts': posts}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def following_users_posts(request):
    users = request.user.profile.following.all()
    posts = []

    for u in users:
        post = Post.objects.get(user=u)
        posts.append(post)

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)


def detail(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        raise Http404('Post Not Found!')

    comments = p.comment_set.order_by('-date')

    context = {
        'post': p,
        'comments': comments
    }
    return render(request, 'detail.html', context)


@login_required(login_url='login')
def edit(request, post_id):
    if request.method == 'POST':
        p = Post.objects.get(id=post_id)
        form = PostCreationForm(request.POST, request.FILES, instance=p)

        if form.is_valid():
            form.save()
            messages.success(request, 'Post has successfully edited')
            return redirect(reverse('detail', args=(p.id,)))

    else:
        p = Post.objects.get(id=post_id)
        form = PostCreationForm(instance=p)

    context = {
        'post': p,
        'form': form
    }
    return render(request, 'edit.html', context)


@login_required(login_url='login')
def delete_post(request, post_id):
    p = Post.objects.get(id=post_id)
    p.delete()

    messages.success(request, 'Post has successfully deleted')
    return redirect('index')


@login_required(login_url='login')
def leave_comment(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        raise Http404('Post Not Found!')

    username = request.user.username
    p.comment_set.create(user=username, text=request.POST.get('text'))

    return redirect(reverse('detail', args=(p.id,)))


@login_required(login_url='login')
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
        else:
            like.save()

    return redirect('index')
