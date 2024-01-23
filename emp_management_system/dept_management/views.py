from django.shortcuts import render
from .models import dept

def dept_list(request):
    departments = dept.objects.all()
    return render(request,'dept_list.html',{'departments':departments})
