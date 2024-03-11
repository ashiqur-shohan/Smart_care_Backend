from django.shortcuts import render
from rest_framework import viewsets,pagination,filters
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from .models import Doctor,Specialization,Designation,AvailableTime,Review
from .serializers import DoctorSerializers,SpecializationSerializers,DesignationSerializers,AvailableTimeSerializers,ReviewSerializers

from rest_framework.routers import DefaultRouter
# Create your views here.


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 #item per page
    page_size_query_param = page_size
    max_page_size = 100 



class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers 
    #next previous button create kora holo
    pagination_class = DoctorPagination
    def get_queryset(self):
        queryset= super().get_queryset()
        doctor_id = self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset = queryset.filter(id=doctor_id)
        return queryset

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializers 


class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializers 

#filter kore niye ashbo time specific doctor er jonno
class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            #available time er sathe doctor er realtion many to many. 
            #realted name diye o access kora jeto
            #small doctor likhar karon holo Doctor model er instance create hoy doctor name a
            return query_set.filter(doctor=doctor_id)
        return query_set


class AvailableTimeViewset(viewsets.ModelViewSet):
    #eita add korar maddhome secure kore fellam 
    # log in user chara ei api use korte parbe na

    # permission_classes = [IsAuthenticated]

    #dekhte parbe kintu edit korte parbe na
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializers 

    # built in keyword
    filter_backends = [AvailableTimeForSpecificDoctor]

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers 
