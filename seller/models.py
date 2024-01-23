from django.db import models

# Create your models here.
class Seller(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    password=models.TextField(max_length=100)
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.TextField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=100,null=True)
    price=models.PositiveIntegerField(null=True)
    image=models.ImageField(null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
