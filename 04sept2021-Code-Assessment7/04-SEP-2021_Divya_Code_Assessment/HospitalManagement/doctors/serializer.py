from django.db.models import fields
from rest_framework import serializers
from doctors.models import Doctors

class DoctorSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Doctors
        fields = ("id","doctor_code","doctor_name","Address","mobile_no","specialization","email_id")