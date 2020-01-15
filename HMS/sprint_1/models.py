from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# a expense model
class Expense(models.Model):
    title = models.CharField(max_length = 20)
    amount = models.BigIntegerField()
    description = models.TextField()
    date = models.DateTimeField(default = timezone.datetime.now)
    def __str__(self):
        return "{}-{}-{}" .format(self.title,self.amount,self.date)
#income model
class Income(models.Model):
    title = models.CharField(max_length = 20)
    amount = models.BigIntegerField()
    description = models.TextField()
    date = models.DateTimeField(default = timezone.datetime.now)
    def __str__(self):
        return "{}-{}-{}" .format(self.title,self.amount,self.date) 
#Employee model
class Employee(models.Model):
    full_name = models.CharField(max_length = 30)
    national_id = models.CharField(max_length = 40)
    date_hired = models.DateTimeField(default = timezone.datetime.now)
    income = models.BigIntegerField()
    last_payment = models.DateTimeField()
    paid = models.BooleanField()
    #check that is the employee paid or not if not change a value in model
    def save(self, *args, **kwargs): 
        now = timezone.datetime.now()
        ptime = self.last_payment
        pdelta = timezone.datetime(ptime.year,ptime.month,ptime.day,ptime.hour,ptime.minute,ptime.microsecond)
        diff = now - pdelta
        if diff.days > 30 :
            self.paid = False    
        super(Employee, self).save(*args, **kwargs) 
    def __str__(self):
        return self.full_name
class Token(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __str__(self):
        return self.user