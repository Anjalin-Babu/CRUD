from django.shortcuts import render,redirect
from .forms import Employee_form
from .models import Employee

def employee_list(request):
    contest={'employee_list':Employee.objects.all()}
    return render(request,'employee_list.html',contest)

def employee_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form=Employee_form()
        else:
            employee= Employee.objects.get(id=id) 
            form = Employee_form(instance=employee)
        return render(request, "employee_form.html", {'j': form})
    
    else:
        
        if id == 0:
            form = Employee_form(request.POST)
        else:
            employee = Employee.objects.get(id=id)
            form = Employee_form(request.POST,instance= employee)
        if form.is_valid(): 
            form.save()
        return redirect('/list') 
    

def employee_delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/list')
