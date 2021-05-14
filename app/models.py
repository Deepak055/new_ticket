from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Employee(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    employee_id=models.IntegerField(primary_key=True)
    employee_name=models.CharField(max_length=30)



def __str__(self):
    return self.user.username





class EndUser(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='profile_pics',blank=True)


def __str__(self):
    return self.user.username



class Supervisor(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    supervisor_id=models.IntegerField(primary_key=True)
    supervisor_name=models.CharField(max_length=30)


def __str__(self):
    return self.user.username



class Customercreation(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=300)
    type=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    priority=models.CharField(max_length=30)
    description=models.TextField(max_length=30)


    def __str__(self):
        return self.user.username
    

