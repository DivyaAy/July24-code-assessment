from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def addpage(request):
    if (request.method == "POST"):
        getF_Name = request.POST.get("Faculty_name")
        getadd = request.POST.get("address")
        getdepart = request.POST.get("department")
        getecollege = request.POST.get("college")
        fac_dict = {"Faculty_name":getF_Name,"address":getadd,"department":getdepart,"college":getecollege};
        result = json.dumps(fac_dict)
        return HttpResponse(result)
    else:
        return HttpResponse("thank you")