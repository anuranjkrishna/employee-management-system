from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):

    search = request.GET.get('search')

    if search:
        employees = Employee.objects.filter(name__icontains=search)
    else:
        employees = Employee.objects.all()

    return render(request, 'home.html', {
        'employees': employees
    })


@login_required
def add_employee(request):

    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'add_employee.html', {
        'form': form
    })


@login_required
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('/')


@login_required
def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'add_employee.html', {
        'form': form
    })