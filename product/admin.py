from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','name','status','created_at']
    save_on_top = True

    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)
