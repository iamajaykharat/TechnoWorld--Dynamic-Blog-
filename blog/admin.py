from django.contrib import admin
from .models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
  fields = ('title', 'slug','content','content1', 'author', 'date','img')
  list_display = ('title', 'author', 'date')
  list_filter = ('title', 'author')
  ordering = ('title',)
  search_fields = ('title', 'author')
