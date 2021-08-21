from re import S
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from books import serializer
from books.serializer import BookSerializer
from books.models import Books
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

def book(request):
    return render(request,'addbook.html')

@csrf_exempt
def addbook(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        book_serializer = BookSerializer(data=mydata)
        if(book_serializer.is_valid()):
            book_serializer.save()
            return JsonResponse(book_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def viewall(request):
    if(request.method == "GET"):
        book = Books.objects.all()
        book_serializer = BookSerializer(book,many=True)
        return JsonResponse(book_serializer.data,safe=False)

@csrf_exempt
def view_single(request,id):
    try:
        book = Books.objects.get(id=id)
    except Books.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        book_serializer = BookSerializer(book)
        return JsonResponse(book_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        book_serializer = BookSerializer(book,data=mydata)
        if(book_serializer.is_valid()):
            book_serializer.save()
            return JsonResponse(book_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "DELETE"):
        book.delete()
        return HttpResponse("Delete item",status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def view_name(request,fetchid):
    try:
        book = Books.objects.get(book_name=fetchid)
    except Books.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        book_serializer = BookSerializer(book)
        return JsonResponse(book_serializer.data,status=status.HTTP_200_OK)
