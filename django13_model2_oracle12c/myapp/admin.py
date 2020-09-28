from django.contrib import admin
from myapp.models import Product

# Register your models here.

class ProductTest(admin.ModelAdmin):
    list_display = ("code", "name", "price", "pub_date")
    
admin.site.register(Product, ProductTest)