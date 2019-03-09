from django import forms
from django.contrib.auth import authenticate
class LoginForm(forms.Form):
    username=forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user=self.cleaned_data.get("username")
        passw=self.cleaned_data.get("password")
        usern=authenticate(username=user,password=passw)
        if usern is None:
            raise forms.ValidationError("wrong credentials")


from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Person
choice=[
    ('--select--','--select--'),
    ('Supervisor','Supervisor'),
    ('TeamLeader','TeamLeader'),
    ('Senior Operator','Senior Operator'),
    ('Skilled Operator','Skilled Operator'),
    ('Semi-Skilled Operator','Semi-Skilled Operator'),
    ('Un-Skilled Operator','Un-Skilled Operator'),
    ('Helper','Helper'),
    ('Trainee','Trainee'),
]


class CustomUserCreationForm(forms.Form):

    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    first_name=forms.CharField(label='Enter Firstname', min_length=4, max_length=150)
    last_name = forms.CharField(label='Enter Lastname', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    desig=forms.ChoiceField(label='Designation',choices=choice)

    class Meta:
        model=User
        fields={'username','first_name','last_name','e-mail','password1','password2','desig'}


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2


    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return user

CHOICES=[('Absent','Absent'),
         ('Present','Present'),
         ('Leave','Leave')
]
class ABC(forms.Form):
    #date =forms.DateField(witxt=forms.CharField()
    Date = forms.DateField(widget = forms.SelectDateWidget)
    Status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

'''def __init__(self, request,*args, **kwargs):

        if not request.user.is_superuser:
            self.fields['Status'].widget.disabled_choices = [3]
        super().__init__(*args, **kwargs)'''

NAMES=[('Any','Any'),
    ('at','at'),
        ('intern','intern'),
       ('ravi','ravi'),
]
class QueryForm(forms.Form):
    name=forms.ModelChoiceField(User.objects.all())
    #name=forms.ChoiceField(choices=User,required=True,label="Names")
    start_date = forms.DateField(required=True,label="Start Date",widget = forms.SelectDateWidget())
    end_date = forms.DateField(required=True,label="Start Date",widget = forms.SelectDateWidget())


import django_tables2 as tables

'''class SimpleTable(tables.Table):
    class Meta:
        model = Person'''

