from django.shortcuts import render, redirect, reverse
from django.http import Http404
from django.contrib import messages

from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.models import User
from .models import Profile
from main.models import Post

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        user_upd_form = UserUpdateForm(request.POST, instance=request.user)
        profile_upd_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_upd_form.is_valid() and profile_upd_form.is_valid():
            user_upd_form.save()
            profile_upd_form.save()

        messages.success(request, 'Account information has been updated!')
        return redirect('profile')

    else:
        user_upd_form = UserUpdateForm(instance=request.user)
        profile_upd_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_upd_form,
        'p_form': profile_upd_form,
        'u': request.user
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def otherProfile(request, u_name):
    try:
        u = User.objects.get(username=u_name)
        if u == request.user:
            return redirect('profile')
    except:
        raise Http404('User not found')

    p = Profile.objects.get(user=u)
    posts = Post.objects.filter(user=u)
    my_profile = Profile.objects.get(user=request.user)

    if p.user in my_profile.following.all():
        follow = True
    else:
        follow = False

    context = {
        'u': u,
        'user_profile': p,
        'posts': posts,
        'follow': follow
    }
    return render(request, 'profile.html', context)


def follow_unfollow(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            if obj.user != my_profile.user:
                my_profile.following.add(obj.user)
            else:
                messages.info(request, 'You can not follow yourself')

        return redirect(reverse('otherprofile', args=(obj.user.username,)))


def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['theme'] = 'dark'
            return redirect('profile')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'login.html')


def logOut(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'You are successfully created an account for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)
