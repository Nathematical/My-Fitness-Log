from django.urls import path
from . import views

app_name = 'log_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('add_exercise/', views.add_exercise, name='add_exercise'),
    path('current_workout/', views.current_workout, name='current_workout'),
    path('workout_history/', views.workout_history, name='workout_history')
]