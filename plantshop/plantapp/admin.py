from django.contrib import admin
from plantapp.models import Product, Contact
from plantapp.models import Cart, CartItems
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(CartItems)
