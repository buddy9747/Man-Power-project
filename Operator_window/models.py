from django.db import models
from django.contrib.auth.models import  User
import datetime

class Production(models.Model):
    value=models.DateTimeField(default=datetime.datetime.now,blank=True)
    serial_no=models.CharField(max_length=10)
    hourly_achieved=models.IntegerField(default=0)
    hourly_running_ticket_no=models.CharField(max_length=10)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

class Quality(models.Model):
    value=models.DateTimeField(default=datetime.datetime.now,blank=True)
    rework_ticket_no=models.CharField(max_length=10)
    repair_ticket_no=models.CharField(max_length=10)
    finish_return_ticket_no=models.CharField(max_length=10)
    cutting_defects_ticket_no=models.CharField(max_length=10)
    cutting_missing_ticket_no=models.CharField(max_length=10)
    holding_ticket_no=models.CharField(max_length=10)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

class Maintenance(models.Model):
    value=models.DateTimeField(default=datetime.datetime.now,blank=True)
    waiting=models.CharField(max_length=5)
    setting=models.CharField(max_length=5)
    breakdown=models.CharField(max_length=5)
    power_failure=models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PlanChange(models.Model):
    value=models.DateTimeField(default=datetime.datetime.now,blank=True)
    machine_issue=models.CharField(max_length=5)
    quality_issue=models.CharField(max_length=5)
    trims_issue=models.CharField(max_length=5)
    others=models.CharField(max_length=5)
    delay_start=models.CharField(max_length=5)
    demo=models.CharField(max_length=5)
    learning=models.CharField(max_length=5)
    full_swing=models.CharField(max_length=5)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
