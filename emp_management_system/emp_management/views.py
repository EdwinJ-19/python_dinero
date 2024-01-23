from django.shortcuts import render
from .models import emp

def emp_list(request):
    employees = emp.objects.all()
    return render(request,'emp.html',{'employees':employees})

