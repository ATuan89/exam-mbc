from django.contrib import admin
from .models import Department, Job

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_code', 'department_name', 'valid')
    list_filter = ('valid',)
    search_fields = ('department_name',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_code', 'job_name', 'valid')
    list_filter = ('valid',)
    search_fields = ('job_name',)