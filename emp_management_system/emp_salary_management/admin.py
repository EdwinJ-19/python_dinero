from django.contrib import admin
from .models import emp_sal

class salaryadmin(admin.ModelAdmin):
    list_display = ('employee','salary_amount','start_date','end_date')
    list_filter = ('employee','start_date','end_date')
    search_fields = ('employee_name',)

admin.site.register(emp_sal, salaryadmin)
