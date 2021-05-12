from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path ('sign', views.index,name='index'),
    path('login/', views.user_login,name='login'), 
    path('logout/', views.user_logout,name='logout'), 
    path('customer_login/', views.customer_login,name='customer_login'), 
    
    path('supervisor_login/', views.supervisor_login,name='supervisor_login'), 
    path('customer/', views.customer,name='customer'),
    path('supervisor/', views.super_visor,name='super_visor'),
    path('', views.home,name='home'),
    path('pro/', views.pro,name='pro'),
    path('supervisor/', views.supervisor,name='supervisor')
    ]