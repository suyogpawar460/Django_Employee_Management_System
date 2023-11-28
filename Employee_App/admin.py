from django.contrib import admin
from Employee_App.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'salary', 'city']
    ordering = ['id']


admin.site.register(Employee, EmployeeAdmin)
