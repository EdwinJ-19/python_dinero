from django.urls import path
from .views import emp_list

urlpatterns = [
    path('employees/',emp_list,name='emp_list')
]