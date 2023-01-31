from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee

def empHome(request):
    
    emps = Employee.objects.all()
    return render(request, "home.html",{
        'emps':emps
    })

def addEmp(request):
    if request.method == "POST":

        #data fetching 
        empId = request.POST.get("empId")
        empName = request.POST.get("empName")
        empPhone = request.POST.get("empPhone")
        empAddress = request.POST.get("empAddress")
        empGender = request.POST.get("empGender")
        empDept = request.POST.get("empDept")

        #create model object and set the data
        emp = Employee()
        emp.emp_id=empId
        emp.emp_name=empName
        emp.emp_phone=empPhone
        emp.emp_address=empAddress
        emp.emp_gender=empGender
        emp.emp_department=empDept
       
        #save the model
        emp.save()
        #prepare msg

        print("Data is comming")
        return redirect("/employee/home")

    return render(request, "addEmp.html",{})

def deleteEmp(request,emp_id):
    print(emp_id)
    emp = Employee.objects.get(id=emp_id)
    emp.delete()
    return redirect("/employee/home")

def updateEmp(request,emp_id):
    emp=Employee.objects.get(id=emp_id)
    return render(request, "updateEmp.html",{
        'emp':emp
    })

def doUpdate(request,emp_id):
    if request.method == 'POST':
        empIdTemp = request.POST.get("empId")
        empName = request.POST.get("empName")
        empPhone = request.POST.get("empPhone")
        empAddress = request.POST.get("empAddress")
        empGender = request.POST.get("empGender")
        empDept = request.POST.get("empDept")

        emp = Employee.objects.get(id=emp_id)

        emp = Employee()
        emp.emp_id=empIdTemp
        emp.emp_name=empName
        emp.emp_phone=empPhone
        emp.emp_address=empAddress
        emp.emp_gender=empGender
        emp.emp_department=empDept

        emp.save()

    return redirect("/employee/home")

