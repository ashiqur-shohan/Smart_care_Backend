from typing import Any
from django.contrib import admin
from .models import Appointment

# email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','patient_name','appointment_types','appointment_status','symptom','time','cancel']

    def patient_name(self,obj):
        return obj.patient.user.first_name
    def doctor_name(self,obj):
        return obj.doctor.user.first_name

    #ami chacchi je admin appoint pending theke change korle jeno user er kache email jay ekta
    #admin panner er kaj korle ei admin a kaj korte hobe
    def save_model(self,request,obj,form,change):
        obj.save()
        # obj holo appointment object ta ke represent kortese
        if obj.appointment_status == 'Running' and obj.appointment_types == 'Online':
            email_subject = "Your Online Appointment is Running."
            email_body = render_to_string('admin_email.html',{'user':obj.patient.user,'doctor':obj.doctor})
            email = EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
        
admin.site.register(Appointment,AppointmentAdmin)