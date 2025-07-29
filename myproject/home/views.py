from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .models import Employee, Department, Job
from django.contrib import messages

def employee_list(request):
    employees = Employee.objects.filter(valid=True)
    return render(request, 'employees/list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        employee = Employee(
            employee_code=request.POST['employee_code'],
            employee_first_name=request.POST['first_name'],
            employee_last_name=request.POST['last_name'],
            gender=int(request.POST['gender']),
            department_code_id=request.POST['department_code'],
            job_code_id=request.POST['job_code'],
            birthday=request.POST['birthday'],
            valid=True
        )
        try:
            employee.save()
            messages.success(request, 'Employee created successfully!')
            return redirect('employee_list')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    departments = Department.objects.filter(valid=True)
    jobs = Job.objects.filter(valid=True)
    return render(request, 'employees/create.html', {'departments': departments, 'jobs': jobs})

def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id, valid=True)
    if request.method == 'POST':
        employee.employee_code = request.POST['employee_code']
        employee.employee_first_name = request.POST['first_name']
        employee.employee_last_name = request.POST['last_name']
        employee.gender = int(request.POST['gender'])
        employee.department_code_id = request.POST['department_code']
        employee.job_code_id = request.POST['job_code']
        employee.birthday = request.POST['birthday']
        try:
            employee.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect('employee_list')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    departments = Department.objects.filter(valid=True)
    jobs = Job.objects.filter(valid=True)
    return render(request, 'employees/update.html', {'employee': employee, 'departments': departments, 'jobs': jobs})

def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id, valid=True)
    if request.method == 'POST':
        employee.valid = False
        employee.save()
        messages.success(request, 'Employee deleted successfully!')
        return redirect('employee_list')
    return render(request, 'employees/delete.html', {'employee': employee})

def employee_sp_create(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    "EXEC sp_InsertEmployee @employee_code=%s, @employee_first_name=%s, "
                    "@employee_last_name=%s, @gender=%s, @department_code=%s, @job_code=%s, @birthday=%s",
                    (
                        request.POST['employee_code'],
                        request.POST['first_name'],
                        request.POST['last_name'],
                        int(request.POST['gender']),
                        request.POST['department_code'],
                        request.POST['job_code'],
                        request.POST['birthday']
                    )
                )
                messages.success(request, 'Employee created successfully!')
                return redirect('employee_list')
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
    departments = Department.objects.filter(valid=True)
    jobs = Job.objects.filter(valid=True)
    return render(request, 'employees/sp_create.html', {'departments': departments, 'jobs': jobs})

def employee_sp_update(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id, valid=True)
    if request.method == 'POST':
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    "EXEC sp_UpdateEmployee @employee_id=%s, @employee_code=%s, @employee_first_name=%s, "
                    "@employee_last_name=%s, @gender=%s, @department_code=%s, @job_code=%s, @birthday=%s",
                    (
                        employee_id,
                        request.POST['employee_code'],
                        request.POST['first_name'],
                        request.POST['last_name'],
                        int(request.POST['gender']),
                        request.POST['department_code'],
                        request.POST['job_code'],
                        request.POST['birthday']
                    )
                )
                messages.success(request, 'Employee updated successfully!')
                return redirect('employee_list')
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
    departments = Department.objects.filter(valid=True)
    jobs = Job.objects.filter(valid=True)
    return render(request, 'employees/sp_update.html', {'employee': employee, 'departments': departments, 'jobs': jobs})

def employee_sp_delete(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id, valid=True)
    if request.method == 'POST':
        with connection.cursor() as cursor:
            try:
                cursor.execute("EXEC sp_DeleteEmployee @employee_id=%s", [employee_id])
                messages.success(request, 'Employee deleted successfully!')
                return redirect('employee_list')
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
    return render(request, 'employees/sp_delete.html', {'employee': employee})