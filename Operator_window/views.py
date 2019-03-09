from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
import dateutil

def prod(request):
    if (request.method=='POST'):
        form=ProductionForm(request.POST)
        if form.is_valid():
            p=form.save(commit=False)
            p.user=User.objects.get(id=request.user.id)
            p.save()
            return HttpResponse('<h1>Saved data </h1>')
        else:
            messages.error(request,'Errors')
    else:
        form=ProductionForm()
        date=Production().value
        #date=date.value
        user=request.user.username
    return render(request,'Operator_window/production.html',{'form':form,'date':date,'name':user})

def quality(request):
    if (request.method=='POST'):
        form=QualityForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = User.objects.get(id=request.user.id)
            p.save()
            return HttpResponse('<h1>Saved data </h1>')
        else:
            messages.error(request,'Errors')
    else:
        form=QualityForm()
        date=Quality().value
    return render(request,'Operator_window/production.html',{'form':form,'date':date})

def main(request):
    if (request.method=='POST'):
        form=MaintenanceForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = User.objects.get(id=request.user.id)
            p.save()
            return HttpResponse('<h1>Saved data </h1>')
        else:
            messages.error(request,'Errors')
    else:
        form=MaintenanceForm()
        date=Maintenance().value
    return render(request,'Operator_window/production.html',{'form':form,'date':date})


def change(request):
    if (request.method=='POST'):
        form=PlanChangeForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = User.objects.get(id=request.user.id)
            p.save()
            return HttpResponse('<h1>Saved data </h1>')
        else:
            messages.error(request,'Errors')
    else:
        form=PlanChangeForm()
        date=PlanChange().value
    return render(request,'Operator_window/production.html',{'form':form,'date':date})



def dash_select(request):
    if (request.method == 'POST'):
        form = Dashselect(request.POST)
        if form.is_valid():
            s = Production.objects.all()
            global name
            name = request.POST.get('user')

            return redirect('/pdash')

        else:
            messages.error(request, "Error")

    else:
        form = Dashselect()
    return render(request, 'Operator_window/dashboard_selection.html', {'form': form})

def pdash(request):
    d = datetime.datetime.now().date()
    e = datetime.datetime.now().time()
    li = Production.objects.filter(user=request.user.id)
    a = []
    n = []
    h=[]
    hh=[]
    effi=[]
    for i in li:
        if (d == i.value.date()):
            a.append(i)
            l = [int(i.serial_no) for i in a]

            for j in range(0, len(l) - 1):
                if (l[j + 1] > l[j]):
                    x = l[j + 1] - l[j]
                else:
                    x = l[j] - l[j + 1]
                n.append(x)
            h = sum([i.hourly_achieved for i in a])
            hh = sum([i.hourly_achieved * 1.05 for i in a])
            effi = h * 1.05 / len(a)
    return render(request, 'Operator_window/production_dashboard.html',
                  {'a': a, 'out': n, 'ha': h, 'ht': hh, 'effi': effi, 'd': d,'e':e})

def qdash(request):
    d = datetime.datetime.now().date()
    e = datetime.datetime.now().time()
    b = Quality.objects.filter(user=request.user.id)
    a=[]
    rw=0
    rp=0
    ft=0
    cd=0
    cm=0
    ht=0
    total=0
    for i in b:
        if(d==i.value.date()):
            a.append(i)
            li=[i.rework_ticket_no for i in a]
            li1=[i.repair_ticket_no for i in a]
            li2=[i.finish_return_ticket_no for i in a]
            li3=[i.cutting_defects_ticket_no for i in a]
            li4=[i.cutting_missing_ticket_no for i in a]
            li5=[i.holding_ticket_no for i in a]
    for j in a:
        s=abs(eval(j.rework_ticket_no))
        if(s>50):
            s=li.count(j.rework_ticket_no)
        rw+=s
        s1=abs(eval(j.repair_ticket_no))
        if(s1>50):
            s1=li1.count(j.repair_ticket_no)
        rp+=s1
        s2=abs(eval(j.finish_return_ticket_no))
        if(s2>50):
            s2=li2.count(j.finish_return_ticket_no)
        ft+=s2
        s3=abs(eval(j.cutting_defects_ticket_no))
        if(s3>50):
            s3=li3.count(j.cutting_defects_ticket_no)
        cd+=s3
        s4=abs(eval(j.cutting_missing_ticket_no))
        if(s4>50):
            s4=li4.count(j.cutting_missing_ticket_no)
        cm+=s4
        s5=abs(eval(j.holding_ticket_no))
        if(s5>50):
            s5=li5.count(j.holding_ticket_no)
        ht+=s5
        total=rw+rp+ft+cd+cm+ht
    return render(request, 'Operator_window/quality_dashboard.html', {'a': a,
                            'd': d,'e':e,'rw':rw,'rp':rp,'ft':ft,'cd':cd,
                                    'cm':cm,'ht':ht,'total':total})

def mdash(request):
    d = datetime.datetime.now().date()
    e = datetime.datetime.now().time()
    b = Maintenance.objects.filter(user=request.user.id)
    a = []
    k = 0
    l = 0
    m = 0
    n = 0
    for i in b:
        if (d == i.value.date()):
            a.append(i)

            for i in a:
                k = k + float(i.waiting)
                l = l + float(i.setting)
                m = m + float(i.breakdown)
                n = n + float(i.power_failure)

            b = k + l + m + n
    return render(request, 'Operator_window/maintenance_dashboard.html',
                  {'a': a, 'k': k, 'l': l, 'm': m, 'n': n, 'b': b, 'd': d, 'e': e})

def pcdash(request):
    d = datetime.datetime.now().date()
    e = datetime.datetime.now().time()
    b = PlanChange.objects.filter(user=request.user.id)
    a = []
    k = 0
    l = 0
    m = 0
    n = 0
    s = 0
    t = 0
    u = 0
    v = 0
    for i in b:
        if (d == i.value.date()):
            a.append(i)

            for i in a:
                k = k + float(i.machine_issue)
                l = l + float(i.quality_issue)
                m = m + float(i.trims_issue)
                n = n + float(i.others)
                s = s + float(i.delay_start)
                t = t + float(i.demo)
                u = u + float(i.learning)
                v = v + float(i.full_swing)
            b = k + l + m + n + s + t + u + v
    return render(request, 'Operator_window/planchange_dashboard.html', {'a': a,
                                                                         'k': k, 'l': l, 'm': m, 'n': n, 's': s, 't': t,
                                                                         'u': u, 'v': v, 'b': b, 'd': d, 'e': e})



