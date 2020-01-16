from django.shortcuts import render
from django.http import JsonResponse 
from json import JSONEncoder
from django.core import serializers
from . import models
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.
@csrf_exempt
def get_unpaid(request):
    if "4" in request.user.get_group_permissions(): #check the permission
        unpaid = models.Employee.objects.filter(paid=False) #Query
        s_unpaid = serializers.serialize("json",unpaid)#serializing
        return JsonResponse(s_unpaid,encoder=JSONEncoder,safe=False) #returning
    else:
        return JsonResponse({"error":"permission denied"},encoder=JSONEncoder)
    
@csrf_exempt
def pay(request):
    if "3" in request.user.get_group_permissions(): #check the permission
        emp = models.Employee.objects.get(national_id = request.POST["national_id"]) #query employee
        models.Expense.objects.create(
            title = "pay employee {}" .format(emp.full_name),
            amount = emp.Income,
            description = request.POST["description"]
        )#create expense
        emp.paid = True
        emp.last_payment = datetime.datetime.now
        emp.save() #update employee data
        return JsonResponse({"result":"payment successfully done!"},encoder=JSONEncoder)
    else:
        return JsonResponse({"error":"permission denied"},encoder=JSONEncoder)