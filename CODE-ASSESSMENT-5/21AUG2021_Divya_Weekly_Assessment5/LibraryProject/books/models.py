from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Books(models.Model):
    book_name =CharField(max_length=50)
    Author =CharField(max_length=50)
    Description =CharField(max_length=50)
    Publisher =CharField(max_length=50) 
    Price =IntegerField()