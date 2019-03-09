from django.db import models
from django.contrib.auth.models import  User
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver


STATUS=[
    ('Absent','Absent'),
    ('Present','Present'),
]
choice=[
    ('--select--','--select--'),
    ('Supervisor','Supervisor'),
    ('TeamLeader','TeamLeader'),
    ('Senior Operator','Senior Operator'),
    ('Skilled Operator','Skilled Operator'),
    ('Semi-Skilled Operator','Semi-Skilled Operator'),
    ('Un-Skilled Operator','Un-Skilled Operator'),
    ('Helper','Helper'),
    ('Trainee','Trainee'),
]

class Person(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField(("Date"), default=date.today)
    status=models.CharField(max_length=10,choices=STATUS)


    def __str__(self):
        return self.name + "     "+ str(self.date)+"      " +self.status

class Employee(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        desig = models.CharField(choices=choice, max_length=20)

        def __str__(self):
            return str(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
    instance.employee.save()
