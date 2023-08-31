from django.contrib import admin
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('f_name','l_name','contact_nu','email')
admin.site.register(Contact,ContactAdmin)


# Register your models here.
