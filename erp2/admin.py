from django.contrib import admin
from .models import ProductModel,Inbound,Inventory



# Register your models here.
admin.site.register(ProductModel)
admin.site.register(Inbound)
admin.site.register(Inventory)