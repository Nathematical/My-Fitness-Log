from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
import django.contrib.auth
from .models import User

def register(request):
    # print(request.method)
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_pw = request.POST['retype_pw']

        # check if user already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'log_users/register.html', {'warning': 'That username already exists.'})
            
        # check if passwords match
        if password != retype_pw:
            return render(request, 'log_users/register.html', {'warning': 'Passwords don\'t match.'})
        
        # create the user and redirct to profile page
        user = User.objects.create_user(username, email, password)
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('log_users:profile'))
    
    return render(request, 'log_users/register.html')


def login(request):
    if request.method == 'POST':
        # retrieve the variables from the form submission
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'log_users/login.html', {'warning': 'Invalid Username or Password.'})
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('log_users:profile'))

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     django.contrib.auth.login(request, user)
        #     return HttpResponseRedirect(reverse('log_users:profile'))
        # else:
        #     return render(request, 'log_users/login.html', {'warning': 'Invalid Username or Password.'})
    return render(request, 'log_users/login.html')


def logout(request):
    return HttpResponse('User logout')

@login_required
def profile(request):
    return render(request, 'log_users/profile.html')