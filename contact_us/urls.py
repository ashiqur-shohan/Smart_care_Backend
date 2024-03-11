from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ContactusViewset
#router create korlam . 
#Routers are used with ViewSets in django rest framework to auto config the urls. Routers provides a simple, quick and consistent way of wiring ViewSet logic to a set of URLs.

router = DefaultRouter()
#router er antena(rupok orthe) create krlm. ekta antena ekta kaj korbe . 
#ekek ta antena ekek ta views ke handle korbe
router.register('', ContactusViewset,)


#auto urls create kore felbe
urlpatterns = [
    path('', include(router.urls)),
]