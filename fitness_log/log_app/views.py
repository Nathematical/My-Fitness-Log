from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Exercise, Workout

def index(request):
    return render(request, 'log_app/index.html')

def main(request):
    return render(request, 'log_app/main.html')

@login_required
def new_workout(request):
    return render(request, 'log_app/workout.html')

@login_required
def workout_history(request):
    return render(request, 'log_app/workout_history.html')