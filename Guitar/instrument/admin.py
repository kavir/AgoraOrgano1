from django.contrib import admin
# Register your models here.
from .models import Guitar , Amp, ElectricGuitar,CartItem,Product,Cart

admin.site.register(Product)
admin.site.register(Guitar)
admin.site.register(Amp)
admin.site.register(ElectricGuitar)
admin.site.register(CartItem)
admin.site.register(Cart)