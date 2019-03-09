from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from Absenteeism.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Person
from .forms import LoginForm,ABC
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Count, Max, Min, Sum
from .forms import QueryForm
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginpage(request):
    myform=LoginForm(request.POST or None)
    if myform.is_valid():
        usern=myform.cleaned_data.get("username")
        passw=myform.cleaned_data.get("password")
        user=authenticate(username=usern,password=passw)
        if user:
            return redirect("/profile")
        else:
            messages.error(request, "Error")
    return render(request,"Absenteeism/login.html",{"form":myform})

def register(request):
    if (request.method=='POST'):
        form =CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            user=form.save()
            user.refresh_from_db()
            user.employee.desig=form.cleaned_data['desig']
            user.save()
            return redirect('/login')
        else:
            messages.error(request, "Error")
    else:
        form= CustomUserCreationForm()

    args={'form':form}
    return render(request,'Absenteeism/signup.html',args)

@login_required
def profile(request):
    if (request.method == 'POST'):
        form = ABC(request.POST)
        if (form.is_valid()):

            obj = Person()
            obj.name = User.objects.get(id=request.user.id).username
            obj.date = form.cleaned_data['Date']
            obj.status = form.cleaned_data['Status']
            a = Person.objects.all().filter(name=request.user.username)
            t = str(obj.date)
            c = 0
            for i in a:
                if (str(i.date) == t):
                    c = c + 1
            if (c == 0):
                obj.save()
                return redirect('/profile/check')
            else:
                c = 0
                return redirect('/profile')


        else:
            messages.error(request, "Error")
    else:
        form = ABC()
        return render(request,'Absenteeism/profile.html',{'form':form})

    args={'user':request.user}
    return render(request,'Absenteeism/profile.html',args)

def check(request):
    a=Person.objects.all().filter(name=request.user.username)
    l=[]
    k=[]
    for i in a:
        l.append((i.date))
        k.append(i.status)

    return render(request,'Absenteeism/check.html',{'data':l,'status':k})
	
	
	
def home(request):
    if request.method == 'POST':
        query_form = QueryForm(request.POST)
        if(query_form.is_valid()):
            clean_query = query_form.cleaned_data
            name=clean_query['name']
            start_date = clean_query['start_date']
            end_date = clean_query['end_date']
            global start_date_str
            start_date_str = helper_start_date(start_date)
            global end_date_str
            end_date_str = helper_end_date(end_date)
            min_date_str = helper_min_date()
            max_date_str = helper_max_date()
            total_hhs = helper_total_hhs(min_date_str, max_date_str)
            brand_list = helper_get_brands()
            average_list=find_average(name)
            context={'name':name,'start_date':start_date_str,'end_date':end_date_str, 'min_date':min_date_str,
                                'max_date':max_date_str,'total_hhs':total_hhs,'brand_list':brand_list,'average':average_list}
            return render(request,'Absenteeism/result.html',context)
            #return redirect('/result')

    else:
        query_form = QueryForm()
        return render(request, 'Absenteeism/home.html', {'query_form': query_form})
		
		
		

##def result(request):
##    return render(request,'Absenteeism/result.html')

    
# ------------ BEGIN HELPER FUNCTIONS ------------ #

def helper_start_date(start_date):
	'''Takes in a datetime object, which may either be typecast from a user-supplied 
	date string or the earliest date found in the data table. Returns the date as a string.'''
	if not start_date:
		start_date_obj = Person.objects.all().aggregate(Min('date'))
		start_date = start_date_obj['date__min']
	else:
		start_date = start_date

	return(start_date)
    

def helper_end_date(end_date):
	'''Takes in a datetime object, which may either be typecast from a user-supplied 
	date string or the latest date found in the data table. Returns the date as a string.'''

	if not end_date:
		end_date_obj = Person.objects.all().aggregate(Max('date'))
		end_date = end_date_obj['date__max']
	else:
		end_date = end_date

	return(end_date)


def helper_min_date():
	'''Does not require an input. Returns the earliest date in the data table.'''

	min_date_obj = Person.objects.all().aggregate(Min('date'))
	min_date_str = min_date_obj['date__min']

	return(min_date_str)


def helper_max_date():
	'''Does not require an input. Returns the latest date in the data table.'''

	max_date_obj = Person.objects.all().aggregate(Max('date'))
	max_date_str = max_date_obj['date__max']

	return(max_date_str)


def helper_total_hhs(min_date, max_date):
	'''Takes in the earliest and latest dates found in the data table.
	Returns the count of distinct households that shopped during that period.'''

	total_hhs = Person.objects.values('name').distinct().count()
	total_hhs = "{:,}".format(total_hhs)
	return(total_hhs)

def helper_get_brands():
	'''Takes in a start date and an end date. If dates are not
	supplied by the user, the earliest and latest dates in the
	table are used. Returns a list of brands purchased within
	the dates specified.'''

	all_brands_qs = Person.objects.filter().values('name').distinct()
	brand_list = []

	for brand in all_brands_qs:
		brand_list.append(brand['name'])

	return(brand_list)


def find_average(n):
    a=Person.objects.filter(name=n)
    c=0
    for i,j in enumerate(a):
        if(j.status=='Absent'):
            c+=1
    i=i+1
    return c/i*100

'''


def top_buying_brand(brands, start_date, end_date):
##	Takes in a list of all brands in the data table, 
##	and start and end dates. Dates are selected by the user, 
##	or the largest available timeframe is used by default. 
##	Returns the average dollars spent per household on each 
##	brand within the timeframe given.

	avg_spend_hh_by_brand = {}

	for brand in brands:

		sum_item_spend = Person.objects.values('brand').filter(date__gte=start_date, 
							date__lte=end_date, brand=brand).annotate(total_spent=Sum('item_spend'))
		
		sum_hhs = Trips.objects.filter(brand=brand,date__gte=start_date,
							date__lte=end_date).values('user_id').distinct().count()
		
		avg_spend_hh = round((sum_item_spend[0]['total_spent'] / sum_hhs), 2)
		
		avg_spend_hh_by_brand[brand] = [avg_spend_hh,"{:,}".format(sum_item_spend[0]['total_spent']), "{:,}".format(sum_hhs)]

	print(avg_spend_hh_by_brand)
	return(avg_spend_hh_by_brand)




'''

def all_att(request):
    x=[]
    y=[]
    z=[]
    m=Person.objects.all()
    #table=SimpleTable(m)
    return render(request, 'Absenteeism/check_attendance.html',{'x':x,'y':y,'z':z,'m':m})