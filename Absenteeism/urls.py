from django.urls import path
from Absenteeism import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    #path('result/',views.result,name='result'),
    path('login/',login,{'template_name':'Absenteeism/login.html'},name='login'),
    path('logout/',logout,{'template_name':'Absenteeism/logout.html'}),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('profile/check/',views.check,name='check'),
    path('home/',views.home,name='home'),
    path('all_attendance',views.all_att),
    
]
