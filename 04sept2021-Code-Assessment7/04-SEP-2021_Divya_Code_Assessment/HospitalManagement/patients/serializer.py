from django.db.models import fields
from rest_framework import serializers
from patients.models import Patients

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields = ("id","patient_code","patient_name","Address","Email_id","Phone","pincode")