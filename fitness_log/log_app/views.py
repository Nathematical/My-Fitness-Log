from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Exercise, Workout

def index(request):
    return render(request, 'log_app/index.html')

def main(request):
    return render(request, 'log_app/main.html')

@login_required
def add_exercise(request):
    if request.method == "POST":
        print(request.POST)
        category = request.POST['category']
        exercise = request.POST['exercise']
        set1_reps = request.POST['set1_reps']
        set2_reps = request.POST['set2_reps']
        set3_reps = request.POST['set3_reps']
        set4_reps = request.POST['set4_reps']
        set1_weight_lifted = request.POST['set1_weight_lifted']
        set2_weight_lifted = request.POST['set2_weight_lifted']
        set3_weight_lifted = request.POST['set3_weight_lifted']
        set4_weight_lifted = request.POST['set4_weight_lifted']
        exercise = Exercise(
            category=category,
            name=exercise,
            set1_reps=set1_reps,
            set2_reps=set2_reps,
            set3_reps=set3_reps,
            set4_reps=set4_reps,
            set1_weight_lifted=set1_weight_lifted,
            set2_weight_lifted=set2_weight_lifted,
            set3_weight_lifted=set3_weight_lifted,
            set4_weight_lifted=set4_weight_lifted,
        )
        exercise.save()


    return render(request, 'log_app/exercise.html')

@login_required
def current_workout(request):
    exercises = Exercise.objects.all()
    context = {
        'exercises': exercises,
    }
    return render(request, 'log_app/current_workout.html', context)


@login_required
def workout_history(request):
    return render(request, 'log_app/workout_history.html')