from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=200)
    emp_name=models.CharField(max_length=200)
    emp_phone = models.CharField(max_length=10)
    emp_address = models.CharField(max_length=200)
    emp_gender = models.CharField(max_length=10)
    emp_department = models.CharField(max_length=100)
    
