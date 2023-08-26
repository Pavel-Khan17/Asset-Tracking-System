from django.urls import path
from . import views

app_name = 'assets'

urlpatterns = [
    
    # url to get and post company instence 
    path('companies/', views.CompanyListCreateView.as_view(), name='company_list'),
    # url to get and post employee instence 
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee_list'),
    # url to get and post assets instence 
    path('assets_list/', views.AssetsListCreateView.as_view(), name='asssets_list'),
    
    # url to get, update, delete each assets instence 
    path('assets_list/<int:id>', views.AssetsUpdateDeleteView.as_view(), name='asssets_update_delete'),
    
    # url to get and post assets log instence 
    path('assets_logs/', views.AssetsLogListCreateView.as_view(), name='assets_log_list'),
    
    # url to update and delete assets log instence 
    path('assets_logs/<int:id>', views.assets_log_detail , name='assets_log_update'),
    
    # url to list the assets log for every company 
    path('assets_logs/company/<str:company_name>/', views.AssetsLogListByCompanyView.as_view(), name='assets_log_list_by_company'),
    
    # url to list the assets log for every employee
    path('assets_logs/employee/<int:employee_id>/', views.AssetsLogListByEmployeeView.as_view(), name='assets_logs_list_by_employee'),

]
