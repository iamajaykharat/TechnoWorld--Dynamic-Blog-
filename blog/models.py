from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class BlogPost(models.Model):
  post_id = models.AutoField(primary_key=True)
  title = models.CharField('Title of Article',max_length=200)
  content = models.TextField('Content of Article')
  content1 = models.TextField('Content of Article(Next)',default="")
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  date = models.DateField('Publish Date')
  slug = models.CharField('Slug for URL',max_length=200)
  img = models.ImageField(upload_to='media/img',default="")

  def __str__(self):
      return self.title

class BlogComment(models.Model):
  comment_id = models.AutoField(primary_key= True)
  comment = models.TextField('Comment on Article')
  user = models.ForeignKey(User, on_delete=models.CASCADE )
  post = models.ForeignKey(BlogPost, on_delete=models.CASCADE )
  parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
  timestamp = models.DateTimeField('Date-Time',default=now)

  def comment_mod(self):
    return self.comment[:20] + "..."
  comment_mod.short_description = 'Comments'

  
