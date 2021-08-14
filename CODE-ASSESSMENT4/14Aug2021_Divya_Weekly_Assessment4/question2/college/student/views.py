from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def addpage(request):
    if (request.method == "POST"):
        getName = request.POST.get("name")
        getaddno = request.POST.get("admission_no")
        getroll_no = request.POST.get("roll_no")
        getecollege = request.POST.get("college")
        getparent_name = request.POST.get("parent_name")
        std_dict = {"name":getName,"admission_no":getaddno,"roll_no":getroll_no,"college":getecollege,"parent_name":getparent_name};
        result = json.dumps(std_dict)
        return HttpResponse(result)
    else:
        return HttpResponse("thank you")