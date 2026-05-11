from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_item, name='report_item'),
    path('listings/', views.listings, name='listings'),
    path('close/<int:item_id>/', views.close_item, name='close_item'),
    path('insights/', views.insights, name='insights'),
    path('employees/', views.employees, name='employees'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('delete_employee/<str:employee_id>/', views.delete_employee, name='delete_employee'),
]