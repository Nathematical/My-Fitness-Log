from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return render(request, 'log_users/register.html')


def login(request):
    return HttpResponse('User Login')


def logout(request):
    return HttpResponse('User logout')


def profile(request):
    return HttpResponse('User Profile')