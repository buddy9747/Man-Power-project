from django.db import models
from Absenteeism.models import *
from django.contrib.auth.models import User
# Create your models here.

cho=[

    ('25%','25%'),
('50%','50%'),
('75%','75%'),
('100%','100%'),

]

class Operat(models.Model):

    type_of_operations = models.CharField(max_length=50)
    opt_weightage = models.IntegerField()
    operation_desc=models.TextField(max_length=500)


    def __unicode__(self):
        return self.type_of_operations
    def __str__(self):
        return self.type_of_operations

class Scale(models.Model):
    level=models.CharField(choices=cho,max_length=50)
    operation = models.ForeignKey(Operat, on_delete=models.CASCADE)
    skill_desc=models.TextField(max_length=1500)
    use = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.use) +"   "+str(self.operation) +"  "+str(self.level)