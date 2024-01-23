from django.urls import path
from .views import salary_list

urlpatterns = [
    path('salaries/',salary_list, name='salary_list')
]