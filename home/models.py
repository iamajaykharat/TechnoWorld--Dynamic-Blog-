from django.db import models

# Create your models here.

class Contact(models.Model):
  
    firstname = models.CharField('First Name',max_length=100)
    lastname = models.CharField('Last Name',max_length=100)
    email = models.EmailField('Email')
    address = models.CharField('Address',max_length=200)
    city = models.CharField('City',max_length=100)
    state = models.CharField('State',max_length=100)
    msg = models.TextField('Query/Feedback')
    rating = models.CharField('Rating',max_length=100)

    def __str__(self):
        return self.firstname +" "+ self.lastname
  
  

