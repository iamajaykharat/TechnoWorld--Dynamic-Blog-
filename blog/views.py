from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BlogPost,BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.

# Blog Home Page
def blogHome(request):
    posts = BlogPost.objects.all()
    return render(request,'blog/blogHome.html',{'posts':posts})

# Blog Post Page
def blogPost(request,slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict={}
    for reply in replies:
        if reply.parent.comment_id not in replyDict.keys():
            replyDict[reply.parent.comment_id] = [reply]
        else:
            replyDict[reply.parent.comment_id].append(reply)


    return render(request, 'blog/blogPost.html', {'post': post, 'comments': comments, 'user': request.user, 'replyDict':replyDict})


# Post comments
def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postId = request.POST.get("postId")
        parentId = request.POST.get("parentId")
        post = BlogPost.objects.get(post_id=postId)

        if parentId == "":
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request, 'Your Comment has been posted Successfully.', extra_tags='toastmsg')
        else:
            parent = BlogComment.objects.get(comment_id=parentId)
            comment = BlogComment(comment=comment, user=user, post=post,parent=parent)
            comment.save()
            messages.success(
                request, 'Your Reply has been posted Successfully.', extra_tags='toastreply')

        return redirect(f'/blog/{post.slug}')

    return redirect(f'/blog/{post.slug}')
