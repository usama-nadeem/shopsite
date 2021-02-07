from django.contrib import admin
from .models import customer

# Register your models here.

#linking Customer panel with admin so that it can be managed through admin panel
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(customer, CustomerAdmin)