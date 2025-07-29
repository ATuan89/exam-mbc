from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:employee_id>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),
    path('employees/sp-create/', views.employee_sp_create, name='employee_sp_create'),
    path('employees/<int:employee_id>/sp-update/', views.employee_sp_update, name='employee_sp_update'),
    path('employees/<int:employee_id>/sp-delete/', views.employee_sp_delete, name='employee_sp_delete'),
]