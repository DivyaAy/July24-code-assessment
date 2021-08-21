from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from librarian.serializer import LibSerializer
from librarian.models import Librarian
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

def reg(request):
    return render(request,'lib.html')
def log(request):
    return render(request,'login.html')

@csrf_exempt
def add(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        lib_serializer = LibSerializer(data=mydata)
        if(lib_serializer.is_valid()):
            lib_serializer.save()
            return JsonResponse(lib_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def viewall(request):
    if(request.method == "GET"):
        librarians = Librarian.objects.all()
        lib_serializer = LibSerializer(librarians,many=True)
        return JsonResponse(lib_serializer.data,safe=False)

@csrf_exempt
def view_single(request,id):
    try:
        librarians = Librarian.objects.get(id=id)
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        lib_serializer = LibSerializer(librarians)
        return JsonResponse(lib_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        lib_serializer = LibSerializer(librarians,data=mydata)
        if(lib_serializer.is_valid()):
            lib_serializer.save()
            return JsonResponse(lib_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    
    if(request.method == "DELETE"):
        librarians.delete()
        return HttpResponse("Deleted item",status=status.HTTP_204_NO_CONTENT)
        
@csrf_exempt
def view_code(request,fetchid):
    try:
        librarians = Librarian.objects.get(enroll_code=fetchid)
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid_id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        lib_serializer = LibSerializer(librarians)
        return JsonResponse(lib_serializer.data,status=status.HTTP_200_OK)