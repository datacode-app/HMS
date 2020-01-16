from . import models
from apscheduler.schedulers.background import BackgroundScheduler
def saving():
    models.Employee.save()
def daily_check(): #save scheduler that do the written methods
    scheduler = BackgroundScheduler()
    scheduler.add_job(saving,'interval',minutes=5)
    