from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.utils import timezone
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Post, Like
from .forms import PostCreationForm, PostCreationFormAdaptive


def index(request):
    if request.method == 'POST':
        try:
            form = PostCreationForm(request.POST, request.FILES)
            form_adaptive = PostCreationFormAdaptive(request.POST, request.FILES)

            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.date = timezone.now()
                post.save()
                return redirect('index')

            elif form_adaptive.is_valid():
                post = form_adaptive.save(commit=False)
                post.user = request.user
                post.date = timezone.now()
                post.save()
                return redirect('index')

        except ValueError:
            return redirect('login')

    posts = Post.objects.order_by('-date')

    form = PostCreationForm()
    form_adaptive = PostCreationFormAdaptive

    context = {'posts': posts, 'form': form, 'form_adaptive': form_adaptive}
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


@login_required(login_url='login')
def edit(request, post_id):
    if request.method == 'POST':
        p = Post.objects.get(id=post_id)
        form = PostCreationForm(request.POST, request.FILES, instance=p)

        if form.is_valid():
            form.save()
            messages.success(request, 'Post has successfully edited')
            return redirect('index')

    else:
        p = Post.objects.get(id=post_id)
        form = PostCreationForm(instance=p)

    context = {
        'post': p,
        'form': form
    }
    return render(request, 'index.html', context)


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

    p.comment_set.create(user=request.user, text=request.POST.get('text'))

    return redirect('index')


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


@login_required(login_url='login')
def theme_switch(request):
    if request.session['theme'] == 'light':
        request.session['theme'] = 'dark'
    else:
        request.session['theme'] = 'light'

    return redirect('index')
