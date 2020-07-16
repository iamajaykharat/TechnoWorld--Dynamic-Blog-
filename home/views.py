from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from blog.models import BlogPost
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Home Page
def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'home/index.html', {'posts': posts})


# About Page
def about(request):
    return render(request, 'home/about.html')


# Contact Form
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

        contact = Contact(firstname=firstname, lastname=lastname, address=address,city=city, state=state, email=email, rating=rating, msg=msg)

        contact.save()
        messages.info(
            request, 'Thank You for Contacting us!, We will respond you shortly. Visit us.')
        return redirect('/contact/')

    return render(request, 'home/contact.html')


# Search System
def search(request):
    query = request.GET['query']
    if len(query) > 120:
        posts = BlogPost.objects.none()
    else:
        postsTitle = BlogPost.objects.filter(title__icontains=query)
        postsContent = BlogPost.objects.filter(content__icontains=query)
        postsContent1 = BlogPost.objects.filter(content1__icontains=query)
        posts1 = postsTitle.union(postsContent)
        posts = postsContent1.union(posts1)
    return render(request, 'home/search.html', {'posts': posts, 'query': query})


# Authentication System-Signup
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not username.isalnum():
            messages.error(
                request, "Username can only contain letters and numbers.", extra_tags='useralnum')
            return redirect('/')

        if len(username) < 3 or len(username) > 15:
            messages.error(
                request, "Length of Username must be greater than 2 and less than 15 characters.", extra_tags='userlen')
            return redirect('/')

        if len(password1) < 4:
            messages.error(
                request, "Passwords must be at least 4 characters in length.", extra_tags='passlen')
            return redirect('/')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, "Username is already in use. Try another Username.", extra_tags='username')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.error(
                    request, "Email is already registerd. Try another Email.", extra_tags='email')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.success(
                    request, "Well Done! You have successfully Join TechnoWorld. Login now!")
                return redirect('/')
        else:
            messages.error(
                request, "Password not matching. Please confirm your Password.", extra_tags='password')
            return redirect('/')

    else:
        return render(request, 'home/index.html')


# Authentication System-Login
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, "Welcome to TechnoWorld! You have successfully logged in.", extra_tags='loginsuccess')
            return redirect('/')
        else:
            messages.error(
                request, "Invalid Credentials! Please try again.", extra_tags='loginerror')
            return redirect('/')
    else:
        return render(request, 'home/index.html')


# Authentication System-Logout
def logout1(request):
    logout(request)
    return redirect('/')
