from patients.views import home
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from requests.sessions import Request
from user.serializer import UserSerializer
from user.models import User
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
import json

# Create your views here.

def loginview(request):
    return render(request,'login.html')
def regview(request):
    return render(request,'register.html')

@csrf_exempt
def user_create(request):
    if(request.method == "POST"):
        user_serializer = UserSerializer(data=request.POST)
        if(user_serializer.is_valid()):
            user_serializer.save()
            return redirect(loginview)
        else:
            return HttpResponse("Error in serializer")
    else:
        return HttpResponse("Get method not allowed")


@csrf_exempt
def login_check(request):
    try:
        getusename = request.POST.get('username')
        getpassword = request.POST.get('password')
        getuser = User.objects.filter(username=getusename,password=getpassword)
        user_serializer = UserSerializer(getuser,many=True)
        print(user_serializer.data)
        if(user_serializer.data):
            for i in user_serializer.data:
                getid = i["id"]
                getname = i["name"]
                getusername = i["username"]
            request.session['uid'] = getid
            request.session['uname'] = getname
            data = {"name":getname,"username":getusername}
            # return HttpResponse(getid)
            #return render(request,'profile.html',{"data":data})
            return redirect(home)
        else:
            return HttpResponse("invalid credientials")

        return HttpResponse(user_serializer.data)
    except User.DoesNotExist:
        return HttpResponse("invalid username")
    except:
        return HttpResponse("something went wrong")