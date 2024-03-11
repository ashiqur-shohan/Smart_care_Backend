from django.contrib import admin
from .models import Specialization,Designation,AvailableTime,Doctor,Review
# Register your models here.

# jehetu specialization a slug use kortesi . auto jeno slug field fill up hoy tar jonno prepopulated field use kora hoy
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}

admin.site.register(Specialization,SpecializationAdmin)

admin.site.register(Designation,DesignationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)