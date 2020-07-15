from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
  post_id = models.AutoField(primary_key= True)
  title = models.CharField('Title of Article',max_length=200)
  content = models.TextField('Content of Article')
  content1 = models.TextField('Content of Article(Next)',default="")
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  date = models.DateField('Publish Date')
  slug = models.CharField('Slug for URL',max_length=200)
  img = models.ImageField(upload_to='media/img',default="")

  def __str__(self):
      return self.title
  
