from django.urls import path
from .views import home, add_employee, delete_employee, edit_employee

urlpatterns = [
    path('',home, name='home'),
    path('add/', add_employee, name='add_employee'),
    path('delete/<int:id>/', delete_employee, name='delete_employee'),
    path('edit/<int:id>/', edit_employee, name='edit_employee'),
]