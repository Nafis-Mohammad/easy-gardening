from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Maintenance)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(ReviewRating)
admin.site.register(WishlistItem)
