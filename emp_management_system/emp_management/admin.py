from django.contrib import admin
from .models import emp

class empadmin(admin.ModelAdmin):
    list_display = ('name','email','address','designation','reporting_manager','department')
    list_filter = ('name','designation','department')
    search_fields = ('name','email','address','designation')

admin.site.register(emp,empadmin)