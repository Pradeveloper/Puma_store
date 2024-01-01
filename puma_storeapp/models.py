from django.db import models
from django.contrib.auth.models import User






# Create your models here.
class Product(models.Model):
            name = models.CharField(max_length=50, verbose_name="product name")
            price = models.FloatField()
            pdetails = models.CharField(max_length=100, verbose_name="Product details")
            CAT=((1,'Bags'),(2,'shoes'),(3,'Watch'))
            cat = models.IntegerField(verbose_name="category", choices=CAT)
            is_active = models.BooleanField(default=True, verbose_name="Availabe")
            pimage=models.ImageField(upload_to='image')

def __str__(self):
     return self.name 

    
class Store(models.Model):
         Uid = models.ForeignKey(User, on_delete=models.CASCADE, db_column="uid")
         Pid = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="pid")
         created_at = models.DateTimeField(auto_now_add=True)
         qty=models.IntegerField(default=1)
         
class Order(models.Model):
    order_id=models.CharField(max_length=30)
    Uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    Pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)