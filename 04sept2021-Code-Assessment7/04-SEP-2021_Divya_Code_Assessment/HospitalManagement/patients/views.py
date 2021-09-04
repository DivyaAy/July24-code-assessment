from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from patients.serializer import PatientSerializer
from patients.models import Patients
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
import json
# Create your views here.

def home(request):
    return render(request,'welcome.html')
def add(request):
    return render(request,'add_detail.html')
def view(request):
    fetchdata = requests.get("http://127.0.0.1:8000/patient/viewall/").json()
    return render(request,'view_detail.html',{"data":fetchdata})
def pa_search(request):
    return render(request,'searching.html')
def pa_update(request):
    return render(request,'updating.html')
def pa_delete(request):
    return render(request,'deleting.html')

@csrf_exempt
def add_value(request):
    if(request.method == "POST"):
        #mydata = JSONParser().parse(request)
        #patient_serializer = PatientSerializer(data=mydata)
        patient_serializer = PatientSerializer(data=request.POST)
        if(patient_serializer.is_valid()):
            patient_serializer.save()
            #return JsonResponse(patient_serializer.data,status=status.HTTP_200_OK)
            return redirect(view)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt 
def view_value(request):
    if(request.method == "GET"):
        patient = Patients.objects.all()
        patient_serializer = PatientSerializer(patient,many=True)
        return JsonResponse(patient_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def view_single(request,id):
    try:
        patient = Patients.objects.get(id=id)
    except Patients.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        patient_serializer = PatientSerializer(patient)
        return JsonResponse(patient_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        patient_serializer = PatientSerializer(patient,data=mydata)
        if(patient_serializer.is_valid()):
            patient_serializer.save()
            return JsonResponse(patient_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "DELETE"):
        patient.delete()
        return JsonResponse("Deleted item",status=status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
def search(request):
    try:
        getpatient_code = request.POST.get("patient_code")
        getpatient = Patients.objects.filter(patient_code = getpatient_code)
        patient_serializer = PatientSerializer(getpatient,many=True)
        return render(request,'searching.html',{"data":patient_serializer.data})
    except Patients.DoesNotExist:
        return HttpResponse("Invalid code",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update(request):
    try:
        getpatient_code = request.POST.get("patient_code")
        getpatient = Patients.objects.filter(patient_code = getpatient_code)
        patient_serializer = PatientSerializer(getpatient,many=True)
        return render(request,'updating.html',{"data":patient_serializer.data})
    except Patients.DoesNotExist:
        return HttpResponse("Invalid code",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update_action(request):
    getnewID = request.POST.get("newID")
    getnewpatient_code = request.POST.get("newpatient_code")
    getnewpatient_name = request.POST.get("newpatient_name")
    getnewAddress = request.POST.get("newAddress")
    getnewEmail_id = request.POST.get("newEmail_id")
    getnewPhone = request.POST.get("newPhone")
    getnewpincode = request.POST.get("newpincode")
    mydata ={"patient_code":getnewpatient_code,"patient_name":getnewpatient_name,"Address":getnewAddress,
    "Email_id":getnewEmail_id,"Phone":getnewPhone,"pincode":getnewpincode}
    jsondata = json.dumps(mydata)
    APIlink = "http://127.0.0.1:8000/patient/viewsingle/"+getnewID
    requests.put(APIlink,data=jsondata)
    return HttpResponse("data has updated successfully")

@csrf_exempt
def delete(request):
    try:
        getpatient_code = request.POST.get("patient_code")
        getpatient = Patients.objects.filter(patient_code = getpatient_code)
        patient_serializer = PatientSerializer(getpatient,many=True)
        return render(request,'deleting.html',{"data":patient_serializer.data})
    except Patients.DoesNotExist:
        return HttpResponse("Invalid code",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def delete_action(request):
    getnewID = request.POST.get("newID")
    APIlink = "http://127.0.0.1:8000/patient/viewsingle/"+getnewID
    requests.delete(APIlink)
    return HttpResponse("data has deleted successfully")