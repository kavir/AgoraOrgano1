from rest_framework import serializers
from .models import Guitar
from .models import CartItem
import base64
class GuitarSerializer(serializers.ModelSerializer):
    image_memory=serializers.SerializerMethodField("get_image_memory")
    price_with_discount=serializers.SerializerMethodField("get_price_with_discount")
    class Meta:
        model=Guitar
        fields=("id","name","price","discount","model","image","preview","last_sold","image_memory","price_with_discount")
    # class Meta:
    #     model=CartItem
    #     fields=("product","quantity")
    
        
    def get_image_memory(request,guitar:Guitar):
        with open(guitar.image.name,'rb') as loadedfile:            
            return base64.b64encode(loadedfile.read())
        
    def get_price_with_discount(request,guitar:Guitar):
        return (guitar.price - (guitar.discount/100)*guitar.price)
        
   
    