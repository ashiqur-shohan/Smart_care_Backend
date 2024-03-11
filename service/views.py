from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.routers import DefaultRouter
# Create your views here.

class ServiceViewset(viewsets.ModelViewSet):
    # model er sokol object ke niye ashlm 
    queryset = Service.objects.all()

    # serializer_class eita built in nam. eitai use kortehbe . eitar maddhome data gulo ke serialize kore fellam . json a convert korlm 
    serializer_class = ServiceSerializer # serializer .py file theke class ta niye ashlm
