from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse('User Registration')


def login(request):
    return HttpResponse('User Login')