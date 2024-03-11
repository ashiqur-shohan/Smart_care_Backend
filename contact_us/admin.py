from django.contrib import admin
from .models import Contact_us
# Register your models here.

# adimin website a data gulo kivhabe show krbe sheita edit krlm
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','problem']


admin.site.register(Contact_us,ContactModelAdmin)
