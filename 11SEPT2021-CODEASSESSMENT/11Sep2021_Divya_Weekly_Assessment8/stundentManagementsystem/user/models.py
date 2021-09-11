from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Userstudent(models.Model):
    name = CharField(max_length=50)
    address = CharField(max_length=50)
    classstd = CharField(max_length=50)
    mobile_number = CharField(max_length=50)
    username = CharField(max_length=50)
    password = CharField(max_length=50)
    