from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'from_date', 'qualification', 'age', 'gender', 'contact', 'address']
admin.site.register(Employee,EmployeeAdmin)

