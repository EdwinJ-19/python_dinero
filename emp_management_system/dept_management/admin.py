from django.contrib import admin
from .models import dept

class deptadmin(admin.ModelAdmin):
    list_display = ('name','floor')
    search_fields = ('name','floor')

admin.site.register(dept, deptadmin)
