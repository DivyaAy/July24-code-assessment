import user
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from requests.sessions import Request
from user.serializer import UserSerializer
from user.models import Userstudent
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import requests
# Create your views here.


def register(request):
    return render(request,'registeruser.html')

def loginuser(request):
    return render(request,'loginuser.html')

# def viewuser(request):
#     fetchdata = requests.get("http://127.0.0.1:8000/user/userview/").json()
#     return render(request,'viewuser.html',{"data":fetchdata})

def viewprofile(request):
    return render(request,'updateprofile.html')

@csrf_exempt
def user_add(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        # user_serializer = UserSerializer(data=mydata)
        user_serializer = UserSerializer(data=request.POST)
        if(user_serializer.is_valid()):
            user_serializer.save()
            # return JsonResponse(user_serializer.data,status=status.HTTP_200_OK)
            return redirect(loginuser)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def user_view(request):
    if(request.method == "GET"):
        users = Userstudent.objects.all()
        user_serializer = UserSerializer(users,many=True)
        return JsonResponse(user_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def user_viewsingle(request,id):
    try:
        users = Userstudent.objects.get(id=id)
    except Userstudent.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        user_serializer = UserSerializer(users)
        return JsonResponse(user_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        user_serializer = UserSerializer(data=mydata)
        if(user_serializer.is_valid()):
            user_serializer.save()
            return JsonResponse(user_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def login_check(request):
    try:
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        getuser = Userstudent.objects.filter(username=getusername,password=getpassword)
        user_serializer = UserSerializer(getuser,many=True)
        print(user_serializer.data)
        if(user_serializer.data):
            for i in user_serializer.data:
                getid = i["id"]
                getname = i["name"]
                getusername = i["username"]
                getpassword = i["password"]
                getaddress = i["address"]
                getclassstd = i["classstd"]
                getmobile_number = i["mobile_number"]
            request.session['uid'] = getid
            request.session['uname'] = getname
            request.session['uusername'] = getusername
            request.session['upassword'] = getpassword
            request.session['uaddress'] = getaddress
            request.session['uclassstd'] = getclassstd
            request.session['umobile_number'] = getmobile_number
            data = {"name":getname,"username":getusername,"password":getpassword,"address":getaddress,"classstd":getclassstd,"mobile_number":getmobile_number}
            # return HttpResponse(getid)
            return render(request,'viewuser.html',{"data":data})
            # return redirect(viewuser)
        else:
            return HttpResponse("Invalid Credientials",status=status.HTTP_404_NOT_FOUND)
        
        return HttpResponse(user_serializer.data)
    except Userstudent.DoesNotExist:
        return HttpResponse("Invalid Username",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update_user(request):
    try:
        # getusername = request.POST.get("username")
        getusername = request.session['uusername']
        getuserid = request.session['uid']
        datas = {"username":getusername,"id":getuserid}
        getuser = Userstudent.objects.filter(datas)
        user_serializer = UserSerializer(getuser,many=True)
        return render(request,'updateprofile',{"data":user_serializer.data})
    except Userstudent.DoesNotExist:
        return HttpResponse("Invlaid username",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Somethig went wrong")

@csrf_exempt
def update_action(request):
    getnewid = request.POST.get("newid")
    getnewusername = request.POST.get("newusername")
    getnewpassword = request.POST.get("newpassword")
    getnnewaddress = request.POST.get("newaddress")
    getnewmobile = request.POST.get("newmobile_number")
    getnewclassstd = request.POST.get("newclassstd")
    mydocs = {"username":getnewusername,"password":getnewpassword,"mobile_number":getnewmobile,"address":getnnewaddress,
    "classstd":getnewclassstd}
    jsondatas = json.dumps(mydocs)
    APIlink = "http://127.0.0.1:8000/user/usersingle/"+getnewid
    requests.put(APIlink,data=jsondatas)
    return JsonResponse("Data has updated successfully",safe=False)