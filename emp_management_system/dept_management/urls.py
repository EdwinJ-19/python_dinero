from django.urls import path
from .views import dept_list

urlpatterns =[
    path('departments/',dept_list,name='dept_list'),
]