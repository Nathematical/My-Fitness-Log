from django.urls import path
from . import views

app_name = 'fitnessapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.index, name='user_login'),
    path('logout/', views.logout, name='user_logout'),
    path('register/', views.register_page, name='register_user'),
]