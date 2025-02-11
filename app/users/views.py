from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm
from .server import my_login


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserLoginForm()
        
    context = {
        'title': 'Авторизация',
        'form': form
    }
        
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    
    context = {
        'title': 'Регистрация',
        'form': form
    }
    
    return render(request, 'users/registration.html', context)
        


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:home'))
