from django.urls import path
from . import views

app_name = 'log_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('new_workout/', views.new_workout, name='newworkout')
]