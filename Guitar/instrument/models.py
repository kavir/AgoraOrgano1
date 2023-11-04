from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    price = models.IntegerField()
    discount = models.IntegerField(default=0, blank=True)
    image = models.ImageField(null=True)
    preview = models.FileField(null=True, blank=True)
    last_sold = models.DateTimeField()
    
    # class Meta:
    #     # abstract = True

    def __str__(self):
        return self.name

class Amp(Product):
    # Add fields specific to the Amp model
    # For example, you can add fields like wattage, number of channels, etc.
    # Example:
    wattage = models.IntegerField()
    channels = models.IntegerField()

class ElectricGuitar(Product):
    # Add fields specific to the ElectricGuitar model
    # For example, you can add fields like number of pickups, body type, etc.
    # Example:
    pickups = models.IntegerField()
    body_type = models.CharField(max_length=100)

class Guitar(Product):
    # Add fields specific to the Guitar model
    # For example, you can add fields like string configuration, body material, etc.
    # Example:
    string_configuration = models.CharField(max_length=10)
    body_material = models.CharField(max_length=100)


# class Amp(models.Model):
#     name=models.CharField(max_length=250)
#     model=models.CharField(max_length=250)
#     price=models.IntegerField()
#     def __str__(self):
#         return self.name
    
    
# class ElectricGuitar(models.Model):
#     name=models.CharField(max_length=250)
#     model=models.CharField(max_length=250)
#     price=models.IntegerField()
#     def __str__(self):
#         return self.name
    
    
# class Guitar(models.Model):
#     name=models.CharField(max_length=250)
#     model=models.CharField(max_length=250)
#     price=models.IntegerField()
#     discount=models.IntegerField(default=0,blank=True)
#     image=models.ImageField(null=True)
#     preview=models.FileField(null=True,blank=True)
#     last_sold=models.DateTimeField()
#     Amp=models.ForeignKey(Amp, on_delete=models.PROTECT,null=True)
#     ElectricGuitar=models.ForeignKey(ElectricGuitar, on_delete=models.PROTECT,null=True)
#     def __str__(self):
#         return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField('Product', through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart for {self.cart.user.username}"
