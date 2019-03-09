from django.urls import path
from leave_calendar import views
from django.contrib.auth.views import login,logout

urlpatterns=[
    path('leave/',views.apply),
    path('get/',views.nun,name='get'),
    path('suggest/',views.suggest,name='leave_suggestion'),
    path('grant/',views.grant,name='grant'),
]