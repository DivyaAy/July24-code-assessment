from django.db.models import fields
from rest_framework import serializers
from user.models import Userstudent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userstudent
        fields = ("id","name","address","classstd","mobile_number","username","password")