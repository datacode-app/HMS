from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class Expense(models.Model):
    title = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    description = models.TextField()
    date  = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return "{}-{}-{}" .format(self.title,self.amount,self.date)
    


class Income(models.Model):
    title = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    description = models.TextField()
    date  = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return "{}-{}-{}" .format(self.title,self.amount,self.date)
    

class Employee(models.Model):
    full_name = models.CharField(max_length=30)
    national_id = models.CharField(max_length=40)
    date_hired = models.DateTimeField(default=datetime.now)
    income = models.BigIntegerField()
    last_payment = models.DateTimeField()
    paid = models.BooleanField()
    def payment(self):
        if abs((self.last_payment-datetime.now).days) > 30:
            self.paid = False
    def __str__(self):
        return self.full_name
    