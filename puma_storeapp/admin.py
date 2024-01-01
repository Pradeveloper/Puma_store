from django.contrib import admin
from puma_storeapp.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
     list_display = ['id', 'name', 'price', 'pdetails', 'cat','is_active']
     list_filter = ['cat', 'price','is_active']

admin.site.register(Product, ProductAdmin)
