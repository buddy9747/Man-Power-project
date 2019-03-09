from django.shortcuts import render
from .models import LeaveApplication
from Absenteeism.models import User
from django.urls import reverse
from .forms import LeaveApplicationForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Absenteeism.models import Employee,Person
from django.http import HttpResponse
import datetime
from .models import LeavePercentage

# Create your views here.

@login_required
def apply(request):
    if (request.method=="POST"):
        form = LeaveApplicationForm(data=request.POST or None)
        if form.is_valid():
            value=form.save(commit=False)
            n=request.user.id
            value.key=Employee.objects.get(user=n)
            value.save()
            return redirect('/get')
        else:
             messages.error(request,"Error")
        current_user = ''
        if request.user.is_authenticated:
         current_user = User.objects.get(user=request.user)
        return render(request, 'leave_calendar/detail.html',
                  {'form': form, 'current_user': current_user}, )
    else:
        form=LeaveApplicationForm()
    e=Employee.objects.get(user=request.user)
    args = {'form': form , 'e':e}
    return render(request, 'leave_calendar/index.html', args)

def fun():
    currdate=(datetime.datetime.now()).date()
    #currdate=currdate[:10]
    b=LeaveApplication.objects.all()
    for i in b:
        if(i.end_date<=currdate):
            le=LeaveApplication.objects.get(id=i.id)
            le.key=None
            print("hi")
            le.save()
                #le=LeaveApplication.objects.get(key=n)
                #print(le)
                #le.key.desig=None
                #le.save()

#global variable
global userid
@login_required
def nun(request):
    fun()
    a=Employee.objects.all()
    l=[i.desig for i in a]
    k=[i.user.username for i in a]
    for j in k:
        if (j==request.user.username):
            #variable=j
            indexvalue=k.index(j)
    #if variable in k:
        #indexvalue=k.index(variable)
    n=l[indexvalue]
    print(n)
    m=[i for i in l if(i==n)]
    c=0
    for i in m:
        print(i)
        c+=1
    print(c)
    b=LeaveApplication.objects.all()
    d=0
    for i in b[:len(b) - 1]:
        print(i)

        if (i.key == None):
            continue
        else:
            print(i.key.desig)
            if (i.key.desig == n):
                d += 1
    print(d)
    e = (d * 100) / c
    print(e)
    j=LeavePercentage.objects.all()
    for i in j:
        x=i.leave_percent
        if (e >= x):
            n = request.user.username
            for i in b:
                if (i.key == None):
                    continue
                else:
                    if (i.key.user.username == n):
                        userid = i.id
            LeaveApplication.objects.get(id=userid).delete()
            return redirect('/suggest')
        else:

            n = request.user.username
            for i in b:
                if (i.key == None):
                    continue
                else:
                    if (i.key.user.username == n):
                        userid = i.id
            l = LeaveApplication.objects.get(id=userid)
            ss = l.start_date
            day = (l.end_date - l.start_date).days + 1
            for i in range(0, day):
                s = Person()
                s.name = n
                s.date = ss
                ss = ss + datetime.timedelta(days=1)
                s.status = "Leave"
                s.save()
            return redirect('/grant')
global f
def grant(request):
    current_user = request.user.username
    l=LeaveApplication.objects.all()
    for i  in l:
        if(i.key==None):
            continue
        else:
            if(i.key.user.username==current_user):
                f=i.id
    b=LeaveApplication.objects.get(id=f)
    x=b.start_date
    y=b.end_date
    return render(request,'leave_calendar/grant.html',{'x':x,'y':y})

def suggest(request):
    currdate = (datetime.datetime.now()).date()
    b = LeaveApplication.objects.all()
    s = set()
    for i in b:
        if (i.key == None):
            continue
        else:
            s.add(i.end_date - currdate)

    x = min(s)
    date = currdate + x
    return render(request, 'leave_calendar/leave_suggestion.html', {'date': date})


    '''current_user = ''
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id).username
    a=Employee.objects.filter(desig=current_user.desig)
    c=0
    for i in a:
        c+=1
    b=LeaveApplication.objects.all()
    d=0
    for i in b:
        if(i.key.desig==request.user):
            d+=1

    e=(d*100)/c
    if(e>=50):
        return HttpResponse("<h1>you are not eligible</h1>")
    else:
        return HttpResponse("<h1>Granted</h1>")'''



