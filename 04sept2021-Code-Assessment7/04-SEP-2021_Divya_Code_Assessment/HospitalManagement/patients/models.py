from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Patients(models.Model):
    patient_code = IntegerField()
    patient_name = CharField(max_length=50)
    Address = CharField(max_length=50)
    Email_id = CharField(max_length=50)
    Phone = CharField(max_length=50)
    pincode = CharField(max_length=50)
    