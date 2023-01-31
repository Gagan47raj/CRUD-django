from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",empHome),
    path("addEmp/",addEmp),
    path("deleteEmp/<int:emp_id>",deleteEmp),  
    path("updateEmp/<int:emp_id>",updateEmp),
    path("doUpdate/<int:emp_id>",doUpdate),    
    path("",empHome),
]