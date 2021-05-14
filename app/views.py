from django.shortcuts import render
from django.urls import reverse
from app.forms import UserForm,EndUserform
from app.forms import employeeform,Supervisorform,Customercreationform
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Customercreation
# Create your views here.

def home(request):
    return render(request,'app/home.html')

def customer(request):
    
    return render(request,'app/customer.html')


def super_visor(request):
    return render(request,'app/supervisor.html')


def employee(request):
    employeeform=Customercreation.objects.all()
    return render(request,'app/employee.html',{'employeeform':employeeform})    



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



def index(request):
    
    
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        employee_form=employeeform(data=request.POST)
        

        if user_form.is_valid() and employee_form.is_valid():
            
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            employee=employee_form.save(commit=False)
            employee.user=user
            employee.save()
            

            registered=True
            
            
        else:
            print(user_form.errors,employee_form.errors)
    else:
        user_form=UserForm()
        employee_form=employeeform()
    return render(request,'app/users.html',{'user_form':user_form,'employee_form':employee_form,'registered':registered})


   

def pro(request):
    
    
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=EndUserform(data=request.POST)
        

        if user_form.is_valid() and profile_form.is_valid():
            
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            
            profile=profile_form.save(commit=False)
            profile.user=user
            
            
            if 'image' in request.FILES:
                profile.image=request.FILES['image']

            profile.save()    

            registered=True
            
            
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=EndUserform()
    return render(request,'app/users1.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

   


def user_login(request):
       
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Account non active')
        else:
            
            print("username:{} and password{}".format(username, password))
            return HttpResponse('invalid login')
    else:
        return render(request,'app/login.html',{})




def customer_login(request):
       
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('customer'))
            else:
                return HttpResponse('Account non active')
        else:
            
            print("username:{} and password{}".format(username, password))
            return HttpResponse('invalid login')
    else:
        return render(request,'app/login.html',{})


def customer_login(request):
       
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('customer'))
            else:
                return HttpResponse('Account non active')
        else:
            
            print("username:{} and password{}".format(username, password))
            return HttpResponse('invalid login')
    else:
        return render(request,'app/login.html',{})


def supervisor_login(request):
       
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('super_visor'))
            else:
                return HttpResponse('Account non active')
        else:
            
            print("username:{} and password{}".format(username, password))
            return HttpResponse('invalid login')
    else:
        return render(request,'app/login.html',{})



def supervisor(request):
    
    
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        supervisor_form=supervisor_form(data=request.POST)
        

        if user_form.is_valid() and supervisor_form.is_valid():
            
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            supervisor=supervisor_form.save(commit=False)
            supervisor.user=user
            supervisor.save()
            

            registered=True
            
            
        else:
            print(user_form.errors,supervisor_form.errors)
    else:
        user_form=UserForm()
        supervisor_form=Supervisorform()
    return render(request,'app/users2.html',{'user_form':user_form,'supervisor_form':supervisor_form,'registered':registered})


def customercreate(request):
    
    
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        customercreation_form=Customercreationform(data=request.POST)
        

        if user_form.is_valid() and customercreation_form.is_valid():
            
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            customer_form=customercreation_form.save(commit=False)
            customer_form.user=user
            customer_form.save()
            

            registered=True
            
            
        else:
            print(user_form.errors,customercreation_form.errors)
    else:
        user_form=UserForm()
        customercreation_form=Customercreationform()
    return render(request,'app/customer.html',{'user_form':user_form,'customercreation_form':customercreation_form,'registered':registered})
