from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'fitnessapp/index.html', context)

def login(request):
    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('users:index/'))
    else:
        return render(request, 'users/login.html', {'message': 'invalid username or password'})


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
