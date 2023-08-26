from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
   list_display =['id','company_name']
   
   
@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
   list_display =['id','company', 'employee_name', 'employee_department']
   
@admin.register(AssetsModel)
class AssetsModelAdmin(admin.ModelAdmin):
   list_display =['id','asset_name', 'asset_manufacturer', 'asset_manufacturer', 'asset_condition', 'asset_issued']
   
@admin.register(AssetsLog)
class AsssetsLogAdmin(admin.ModelAdmin):
   list_display =['id','asset', 'employee', 'checkout_date','return_date', 'checkout_condition','return_condition']