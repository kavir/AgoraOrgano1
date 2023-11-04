from django.shortcuts import render
from rest_framework import generics
from .models import Guitar
from .serializer import GuitarSerializer

##################
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import CartItem
from django.shortcuts import get_object_or_404
# Create your views here.


class GuitarListView(generics.ListAPIView):    
    queryset=Guitar.objects.all()
    serializer_class= GuitarSerializer



############
def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Product, id=product_id)  # Replace 'Product' with your actual product model

    # Get the user's cart or create one if it doesn't exist
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += quantity
        cart_item.save()

    return JsonResponse({'message': 'Item added to cart successfully'})





#############
