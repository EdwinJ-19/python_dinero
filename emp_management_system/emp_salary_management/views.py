from django.shortcuts import render
from .models import emp_sal

def salary_list(request):
    salaries = emp_sal.objects.all()
    return render(request,'emp_salary.html',{'salaries':salaries})
