from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.routers import DefaultRouter
# Create your views here.

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    #custom query korar jonno 
    #built-in function
    #jodi kono patient id diye search kora lage tahole 
    def get_queryset(self):
        #jehetu query set ager theke chilo. oita ke change kortesi. tai super diye queryset ke inherite kore nicchi. var nam ta nijer iccha. 
        # ekhane 7 num line ke niye ashchi 
        queryset = super().get_queryset()
        # patient_id niye ashlam
        patient_id = self.request.query_params.get('patient_id')
        # jodi patient_id khuje tahole e shudhu overwrite korbe.
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        # jodi query na thake thaole 7 num line kei return kore dibe 
        return queryset
        
