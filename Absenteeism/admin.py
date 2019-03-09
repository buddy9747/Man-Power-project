from django.contrib import admin

# Register your models here.
from .models import  Person
from .models import Employee
admin.site.register(Person)
admin.site.register(Employee)