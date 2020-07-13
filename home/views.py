from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world Mainhome')

def about(request):
    return HttpResponse('Hello world about')

def contact(request):
    return HttpResponse('Hello world contact')
