from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BlogPost,BlogComment

# Create your views here.

# Blog Home Page
def blogHome(request):
    posts = BlogPost.objects.all()
    return render(request,'blog/blogHome.html',{'posts':posts})

# Blog Post Page
def blogPost(request,slug):
    post = BlogPost.objects.filter(slug=slug)
    comments = BlogComment.objects.filter(post=post)
    return render(request,'blog/blogPost.html',{'post':post,'comments':comments})


# Post comments
def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postId = request.POST.get("postId")
        post = BlogPost.objects.get(post_id=postId)
        comment = BlogComment(comment=comment,user=user,post=post)
        comment.save()

    return redirect(f'/blog/{post.slug}')