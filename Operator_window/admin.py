from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Production)
admin.site.register(Maintenance)
admin.site.register(Quality)
admin.site.register(PlanChange)