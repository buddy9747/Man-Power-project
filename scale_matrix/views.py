from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ScaleForm
from django.contrib import messages
from django.contrib.auth.models import User
from Absenteeism.models import Employee
from .models import Scale,Operat
from django_tables2 import RequestConfig

# Create your views here.
@login_required
def skill(request):
    if (request.method=="POST"):
        form = ScaleForm(data=request.POST or None)
        if form.is_valid():
            value = form.save(commit=False)
            n = request.user.id
            value.key = Employee.objects.get(user=n)
            value.save()
            return redirect('/skill')
        else:
             messages.error(request,"Error")
        current_user = ''
        if request.user.is_authenticated:
         current_user = User.objects.get(user=request.user)
        return render(request, 'scale_matrix/skill.html',
                  {'form': form, 'current_user': current_user}, )
    else:
        form=ScaleForm()
    e=Employee.objects.get(user=request.user)
    args = {'form': form ,'e':e}
    return render(request, 'scale_matrix/skill.html', args)

@login_required
def skill_view(request):
    #a = User.objects.all().get(username=request.user)
    leve=Scale.objects.filter(use=request.user.id)
    l = []
    k = []
    for i in leve:
        l.append((i.level))
    for j in leve:
        k.append(j.operation)

    return render(request, 'scale_matrix/skill_view.html', {'level': l, 'top': k})

def all_skill(request):
    table = Scale.objects.all()
    #table = SimpleTable(table)
    return render(request, 'scale_matrix/all_skill.html',{'table':table})