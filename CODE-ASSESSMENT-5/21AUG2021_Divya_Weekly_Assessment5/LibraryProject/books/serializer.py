from django.db.models import fields
from rest_framework import serializers
from books.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields = ("book_name","Author","Description","Publisher","Price")