import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Position, Employee
from .forms import StaffForm, PositionForm


def validator(word: str):
    if word[0].islower():
        return False
    return word.isalpha()


def staff_list(request):
    employees = Employee.objects.all()
    return render(request, 'staff/staff_list.html', {'employees': employees})


def staff_add(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        date_of_employment = request.POST.get('date_of_employment')
        if (date_of_employment < str(datetime.date.today())) and validator(surname) and validator(
                name) and validator(patronymic):
            form.save()
            return redirect('list')
        else:
            return HttpResponse('Ошибка в заполнение формы')
    else:
        form = StaffForm()
        return render(request, 'staff/add_form.html', {'form': form})


def staff_change(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        surname = request.POST.get("surname")
        name = request.POST.get("name")
        patronymic = request.POST.get("patronymic")
        position = request.POST.get("position")
        date_of_employment = request.POST.get("date_of_employment")

        if (date_of_employment < str(datetime.date.today())) and validator(surname) and validator(
                name) and validator(patronymic):
            employee.surname = surname
            employee.name = name
            employee.patronymic = patronymic
            position_sql = get_object_or_404(Position, name=position)
            employee.position = position_sql
            employee.date_of_employment = date_of_employment
            employee.save()
            return redirect('list')
        else:
            return HttpResponse('Ошибка в заполнение формы')

    else:
        date = str(employee.date_of_employment)
        positions = Position.objects.all()
        return render(request, 'staff/staff_change.html', {'employee': employee, 'positions': positions, 'date': date})


def staff_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('list')


def all_positions(request):
    positions = Position.objects.all()
    return render(request, 'staff/positions_list.html', {'positions': positions})


def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        name = request.POST.get("name")
        if validator(name):
            form.save()
            return redirect('positions_list')
        else:
            return HttpResponse('Ошибка в заполнение формы')
    else:
        form = PositionForm()
        return render(request, 'staff/add_form.html', {'form': form})


def change_position(request, id):
    position = get_object_or_404(Position, id=id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if validator(new_name):
            position.name = new_name
            position.save()
            return redirect('positions_list')
        else:
            return HttpResponse('Ошибка в заполнение формы')
    else:
        return render(request, 'staff/position_change.html', {'position': position})


def delete_position(request, id):
    position = get_object_or_404(Position, id=id)
    position.delete()
    return redirect('positions_list')
