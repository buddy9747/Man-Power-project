from django.urls import path
from Operator_window import views
urlpatterns=[
    path('prod/', views.prod, name='prod'),
    path('quality/', views.quality, name='quality'),
    path('main/', views.main, name='main'),
    path('change/', views.change, name='change'),
    path('dashselect',views.dash_select,name='dashselect'),
    path('pdash',views.pdash,name='pdash'),
    path('qdash',views.qdash,name='qdash'),
    path('mdash',views.mdash,name='mdash'),
    path('pcdash',views.pcdash,name='pcdash'),
]