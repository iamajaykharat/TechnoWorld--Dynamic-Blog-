from django.contrib import admin
from blog.models import BlogPost
from blog.models import BlogComment

# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'content1', 'author', 'date', 'img')
    list_display = ('title', 'author', 'date')
    list_filter = ('title', 'author')
    ordering = ('title',)
    search_fields = ('title', 'author')


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('comment_mod', 'user','post', 'timestamp')
    ordering = ('comment',)
    search_fields = ('user', 'comment')



