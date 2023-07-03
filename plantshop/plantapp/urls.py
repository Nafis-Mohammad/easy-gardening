from django.urls import path
from plantapp import views
from .models import Cart
from .views import carts, store, checkout


urlpatterns = [
    # jump to views
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('cart/', Cart, name="cart"),
    path('carts', carts, name="carts"),
    path('store', store, name="store"),
    path('checkout', checkout, name="checkout")

]
