from django.contrib import admin
from .models import *

class AdminPlants(admin.ModelAdmin):
    list_display=['name','price','category']
class AdminCustomer(admin.ModelAdmin):
    list_display=['name','email','phone']
class AdminOrder(admin.ModelAdmin):
    list_display=['customer','plants','status']
admin.site.register(Customer,AdminCustomer)
admin.site.register(Plants,AdminPlants)
admin.site.register(Order,AdminOrder)
admin.site.register(Tag)



# Register your models here.
