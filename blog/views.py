from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blogHome(request):
    return HttpResponse('Hello world BlogHome')

def blogPost(request,slug):
    return HttpResponse(f'Hello world BlogPost {slug}')
