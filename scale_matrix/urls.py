from django.urls import path
from scale_matrix import views
from django.contrib.auth.views import login,logout

urlpatterns=[
    path('skill/',views.skill),
    path('skill_view/',views.skill_view),
    path('all_skill/',views.all_skill),
]