from django.http import HttpResponse
from django.shortcuts import render, redirect

from Employee_App.forms import EmployeeModelForm, EmployeeForm
from Employee_App.models import Employee


# Create your views here.
def home_view(request):
    emp = {
        "message": "Welcome to Employee project"
    }
    return render(request, 'home.html', emp)


def createemployee_view(request):
    if request.method == "POST":
        ename = request.POST.get('ename')
        salary = request.POST.get('salary')
        city = request.POST.get('city')

        # emp = Employee(ename=ename, salary=salary, city=city)
        # emp.save()
        Employee.objects.create(ename=ename, salary=salary, city=city)
        # INSERT INTO employee (ename, salary, city) values ('Virat', 20000.0, 'Delhi')

        # return HttpResponse('Employee Data Created Successfully')

        # return render(request, 'success.html')
        # return redirect(employee_list_view)
        return redirect('/employees/list/')

    else:
        return render(request, 'createemployee.html')


def employee_list_view(request):
    list_employee = Employee.objects.all()
    context = {
        "list_employee": list_employee
    }
    return render(request, 'employee_list.html', context)


def CreateEmployee_FormView(request):
    if request.method == 'POST':
        ename = request.POST.get('ename')
        salary = request.POST.get('salary')
        city = request.POST.get('city')

        Employee.objects.create(ename=ename, salary=salary, city=city)

        return redirect('list_employee')

    else:
        form = EmployeeForm()
        context = {"form": form}
        return render(request, 'create_employee_form.html', context)


def CreateEmployee_ModelFormView(request):
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
        else:
            return HttpResponse("Model Form Object data not added")
    else:
        form = EmployeeModelForm()
        context = {"form": form}
        return render(request, 'create_employee_modelform.html', context)
