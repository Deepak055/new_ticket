from django import forms
from django.contrib.auth.models import User
from . models import Employee,EndUser,Supervisor


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model=User
        fields=('username', 'email', 'password')

class employeeform(forms.ModelForm):
    
    class Meta:
        model=Employee
        fields=('employee_id', 'employee_name')


class EndUserform(forms.ModelForm):

    class Meta:
        model=EndUser
        fields=('image',)


class Supervisorform(forms.ModelForm):

    class Meta:
        model=Supervisor
        fields=('supervisor_id','supervisor_name')   
