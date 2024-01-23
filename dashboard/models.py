from django.db import models
from seller.models import Product

# Create your models here.
class Customer(models.Model):
    name=models.TextField(db_column='name',null=True)
    mob=models.BigIntegerField(db_column='mob',null=True)
    email=models.TextField(db_column='email',null=True)
    repass=models.TextField(db_column='password',null=True)


class Contactus(models.Model):       
        name=models.TextField(db_column='name',null=True)
        email=models.TextField(db_column='email',null=True)
        message=models.TextField(db_column='message',null=True)
        
class Cart(models.Model):
      customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
      product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
      quantity=models.PositiveIntegerField(default=1)
