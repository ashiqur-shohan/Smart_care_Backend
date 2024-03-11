from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AppointmentViewset

router = DefaultRouter()
router.register('', AppointmentViewset,)


#auto urls create kore felbe
urlpatterns = [
    path('', include(router.urls)),
]