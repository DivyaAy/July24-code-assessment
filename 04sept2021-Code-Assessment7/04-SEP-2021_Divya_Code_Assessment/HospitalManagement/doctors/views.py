from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from doctors.serializer import DoctorSerilaizer
from doctors.models import Doctors
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
import json
# Create your views here.
def doc_home(request):
    return render(request,'homedoc.html')
def doc_insert(request):
    return render(request,'insert_detail.html')
def doc_show(request):
    fetchdata = requests.get("http://127.0.0.1:8000/doctor/showall/").json()
    return render(request,'show_detail.html',{"data":fetchdata})
def doc_search(request):
    return render(request,'search_detail.html')
def doc_update(request):
    return render(request,'update_detail.html')
def doc_delete(request):
    return render(request,'delete_detail.html')


@csrf_exempt
def insert_detail(request):
    if(request.method == "POST"):
        #mydata = JSONParser().parse(request)
        #doctor_serializer = DoctorSerilaizer(data=mydata)
        doctor_serializer = DoctorSerilaizer(data=request.POST)
        if(doctor_serializer.is_valid()):
            doctor_serializer.save()
            #return JsonResponse(doctor_serializer.data,status=status.HTTP_200_OK)
            return redirect(doc_show)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def showall(request):
    if(request.method == "GET"):
        doctor = Doctors.objects.all()
        doctor_serializer = DoctorSerilaizer(doctor,many=True)
        return JsonResponse(doctor_serializer.data,safe=False,status=status.HTTP_200_OK)
    
@csrf_exempt
def view_one(request,id):
    try:
        doctor = Doctors.objects.get(id=id)
    except Doctors.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        doctor_serializer = DoctorSerilaizer(doctor)
        return JsonResponse(doctor_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        doctor_serializer = DoctorSerilaizer(doctor,data=mydata)
        if(doctor_serializer.is_valid()):
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialzier",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "DELETE"):
        doctor.delete()
        return JsonResponse("Deleted item",status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def find(request):
    try:
        getdoctor_code = request.POST.get("doctor_code")
        getdoctor = Doctors.objects.filter(doctor_code=getdoctor_code)
        doctor_serializer = DoctorSerilaizer(getdoctor,many=True)
        return render(request,"search_detail.html",{"data":doctor_serializer.data})
    except Doctors.DoesNotExist:
        return HttpResponse("Invalid code",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_one(request):
    try:
        getdoctor_code = request.POST.get("doctor_code")
        getdoctor = Doctors.objects.filter(doctor_code=getdoctor_code)
        doctor_serializer = DoctorSerilaizer(getdoctor,many=True)
        return render(request,"update_detail.html",{"data":doctor_serializer.data})
    except Doctors.DoesNotExist:
        return HttpResponse("Invalid code",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def up_action(request):
    getnewid = request.POST.get("newid")
    getnewdoctor_code = request.POST.get("newdoctor_code")
    getnewdoctor_name = request.POST.get("newdoctor_name")
    getnewAddress = request.POST.get("newAddress")
    getnewmobile_no = request.POST.get("newmobile_no")
    getnewspecialization = request.POST.get("newspecialization")
    getnewemail_id = request.POST.get("newemail_id")
    mydatadoc = {"doctor_code":getnewdoctor_code,"doctor_name":getnewdoctor_name,"Address":getnewAddress,
    "mobile_no":getnewmobile_no,"specialization":getnewspecialization,"email_id":getnewemail_id}
    jsondatadoc = json.dumps(mydatadoc)
    APilink = "http://127.0.0.1:8000/doctor/showone/"+getnewid
    requests.put(APilink,data=jsondatadoc)
    return JsonResponse("data has updated successfully",safe=False)

@csrf_exempt
def delete_one(request):
    try:
        getdoctor_code = request.POST.get("doctor_code")
        getdoctor = Doctors.objects.filter(doctor_code=getdoctor_code)
        doctor_serializer = DoctorSerilaizer(getdoctor,many=True)
        return render(request,"delete_detail.html",{"data":doctor_serializer.data})
    except Doctors.DoesNotExist:
        return HttpResponse("Invalid code",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def del_action(request):
    getnewid = request.POST.get("newid")
    APilink = "http://127.0.0.1:8000/doctor/showone/"+getnewid
    requests.delete(APilink)
    return HttpResponse("data has deleted successfully")