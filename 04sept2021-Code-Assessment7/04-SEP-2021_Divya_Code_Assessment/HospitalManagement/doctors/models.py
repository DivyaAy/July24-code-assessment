from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Doctors(models.Model):
    doctor_code = IntegerField()
    doctor_name = CharField(max_length=50)
    Address = CharField(max_length=50)
    mobile_no = CharField(max_length=50)
    specialization = CharField(max_length=50)
    email_id = CharField(max_length=50)
    