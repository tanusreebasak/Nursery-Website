from django.contrib import admin
from .models import *

class AdminPlants(admin.ModelAdmin):
    list_display=['name','plant_id','price','category']
class AdminCustomer(admin.ModelAdmin):
    list_display=['name','email','phone']
class AdminOrder(admin.ModelAdmin):
    list_display=['customer','plants','status']
class AdminCartOrders(admin.ModelAdmin):
    list_display=['customer','plants','status','date','quantity','phone','address']
admin.site.register(Customer,AdminCustomer)
admin.site.register(Plants,AdminPlants)
admin.site.register(Order,AdminOrder)
admin.site.register(Tag)
admin.site.register(CartOrders,AdminCartOrders)



# Register your models here.
