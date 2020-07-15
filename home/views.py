from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from blog.models import BlogPost
from django.contrib import messages

# Create your views here.

def index(request):
    posts = BlogPost.objects.all()
    return render(request,'home/index.html',{'posts':posts})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        msg = request.POST.get('msg')

        contact = Contact(firstname=firstname,lastname=lastname,address=address,city=city,state=state,email=email,rating=rating,msg=msg)

        contact.save()
        messages.info(request,'Thank You for Contacting us!, We will respond you shortly. Visit us.')
        return redirect('/contact/')

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>120:
        posts = BlogPost.objects.none()
    else:
        postsTitle = BlogPost.objects.filter(title__icontains=query)
        postsContent = BlogPost.objects.filter(content__icontains=query)
        postsContent1 = BlogPost.objects.filter(content1__icontains=query)
        posts1 = postsTitle.union(postsContent)
        posts = postsContent1.union(posts1)
    return render(request,'home/search.html',{'posts':posts,'query': query})