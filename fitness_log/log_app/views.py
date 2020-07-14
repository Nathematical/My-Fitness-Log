from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the index page.')

def main(request):
    return render(request, 'log_app/main.html')