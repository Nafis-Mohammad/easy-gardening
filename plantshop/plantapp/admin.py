from django.contrib import admin
<<<<<<< HEAD
from plantapp.models import Product,Contact
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
=======
from plantapp.models import Product, Contact
from plantapp.models import Cart, CartItems
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(CartItems)
>>>>>>> a1cfe3135fb2b4a09571e81750125c86d237723d
