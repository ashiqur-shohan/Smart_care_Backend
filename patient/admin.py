from django.contrib import admin
from .models import Patient
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile_no','image']

    # ekhane user er sathe jehetu ekta relation ache.
    # tai name paoar jonno function likhe data ber kore niye ashte hbe 
    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(Patient,PatientAdmin)