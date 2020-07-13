from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
import django.contrib.auth

def register(request):
    # print(request.method)
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_pw = request.POST['retype_pw']

        if User.objects.filter(username=username).exists():
            return render(request, 'log_users/register.html', {'warning': 'That username already exists.'})

        if password != retype_pw:
            return render(request, 'log_users/register.html', {'warning': 'Passwords don\'t match.'})

        user = User.objects.create_user(username, email, password)
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('log_users:profile'))
    
    return render(request, 'log_users/register.html')


def login(request):
    return HttpResponse('User Login')


def logout(request):
    return HttpResponse('User logout')


def profile(request):
    return HttpResponse('User Profile')