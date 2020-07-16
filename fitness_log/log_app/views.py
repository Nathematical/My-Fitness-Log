from django.shortcuts import render
from django.http import HttpResponse
# from .models import Exercise

def index(request):
    return HttpResponse('This is the index page.')

def main(request):
    return render(request, 'log_app/main.html')

def new_workout(request):
    return render(request, 'log_app/workout.html')

def workout_history(request):
    return render(request, 'log_app/workout_history.html')