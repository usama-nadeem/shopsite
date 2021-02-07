from django.contrib import admin
from .models import product

# Register your models here.

#linking Customer panel with admin so that it can be managed through admin panel
class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(product, ProductAdmin)