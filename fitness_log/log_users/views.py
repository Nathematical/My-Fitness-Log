from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def register(request):
    # print(request.method)
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pasword']
        retype_pw = request.POST['retype_pw']

        if password != retype_pw:
            return render(request, 'log_user/register.html', )

        user = User.objects_user(username, email, password)
    return render(request, 'log_users/register.html', {'warning': 'Passwords don\'t match.'})


def login(request):
    return HttpResponse('User Login')


def logout(request):
    return HttpResponse('User logout')


def profile(request):
    return HttpResponse('User Profile')