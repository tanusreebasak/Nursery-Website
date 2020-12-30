from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)    
    email = models.CharField(max_length=200,null=True) 
    phone = models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField(default="default_profile_pic.png",null=True,blank=True) 
    def __str__(self):  
        return self.name
        

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Plants(models.Model):
    CATEGORY = (
     ('Flower','Flower'),
     ('Fruits','Fruits'),
     ('Vegetables','Vegetables'),
    )
    name = models.CharField(max_length=200,null=True)
    plant_id = models.IntegerField(max_length=200)
    price = models.FloatField(max_length=200)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    image = models.ImageField(default="rose.jpg",null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
     ('Pending','Pending'),
     ('Out for Delivery','Out for Delivery'),
     ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    plants = models.ForeignKey(Plants,null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)    
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    note = models.CharField(max_length=1000,null=True)
    '''
    def __str__(self):
        return self.plants.name'''


