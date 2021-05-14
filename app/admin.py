from django.contrib import admin
from .models import Employee
from .models import EndUser
from .models import Supervisor,Customercreation
# Register your models here.
admin.site.register(Employee)
admin.site.register(EndUser)
admin.site.register(Supervisor)
admin.site.register(Customercreation)
