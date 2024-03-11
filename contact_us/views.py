from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact_us
from .serializers import ContactUsSerializer
from rest_framework.routers import DefaultRouter
# Create your views here.

class ContactusViewset(viewsets.ModelViewSet):
    # model er sokol object ke niye ashlm 
    queryset = Contact_us.objects.all()

    # serializer_class eita built in nam. eitai use kortehbe . eitar maddhome data gulo ke serialize kore fellam . json a convert korlm 
    serializer_class = ContactUsSerializer # serializer .py file theke class ta niye ashlm
