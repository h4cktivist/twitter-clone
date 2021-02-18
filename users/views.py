from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')


def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
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
