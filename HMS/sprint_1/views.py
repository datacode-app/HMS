from django.shortcuts import render
from django.http import JsonResponse 
from json import JSONEncoder
from django.core import serializers
from . import models
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def get_unpaid(request):
    if "4" in request.user.get_group_permissions(): #check the permission
        unpaid = models.Employee.objects.filter(paid=False) #Query
        s_unpaid = serializers.serialize("json",unpaid)#serializing
        return JsonResponse(s_unpaid,encoder=JSONEncoder,safe=False) #returning
    else:
        return JsonResponse({"error":"permission denied"},encoder=JSONEncoder)
    