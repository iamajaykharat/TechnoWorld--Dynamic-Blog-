from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.


def blogHome(request):
    posts = BlogPost.objects.all()
    return render(request,'blog/blogHome.html',{'posts':posts})

def blogPost(request,slug):
    post = BlogPost.objects.filter(slug=slug)
    return render(request,'blog/blogPost.html',{'post':post})
