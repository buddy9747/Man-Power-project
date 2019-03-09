from django.db import models
from django.contrib.auth.models import User
from Absenteeism.models import Employee
# Create your models here.
ch=[
    ('medical leave','medical leave'),
    ('casual leave','casual leave'),
    ('formal leave','formal leave'),
]

class LeavePercentage(models.Model):
    leave_percent=models.IntegerField()

    def __str__(self):
        return str(self.leave_percent)

class LeaveApplication(models.Model):

    start_date=models.DateField()
    end_date=models.DateField()
    leave_reason=models.TextField()
    leave_category=models.CharField(choices=ch,max_length=30)
    leave_percnt=models.ForeignKey(LeavePercentage,on_delete=models.CASCADE,null=True)
    no_of_days=models.IntegerField(null=True)
    key=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    leave_id=models.IntegerField()


    def __str___(self):
        return str(self.key.user)


