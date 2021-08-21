from django.db import models
from django.db.models.fields import BigIntegerField, CharField, IntegerField

# Create your models here.
class Librarian(models.Model):
    enroll_code =IntegerField(default=False)
    name =CharField(max_length=50,default=False)
    address = CharField(max_length=50,default=False)
    mobile_number =BigIntegerField(default=False)
    username = CharField(max_length=50,default=False)
    password = CharField(max_length=50,default=False)
