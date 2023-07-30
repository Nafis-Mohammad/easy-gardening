from django.urls import path
from plantapp import views

from .views import carts, store, checkout, processOrder


urlpatterns = [
    # jump to views
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('carts', views.carts, name="carts"),
    path('store', views.store, name="store"),
    path('collection', views.collection, name="collection"),
    path('collection/<str:id>', views.collectionview, name="collectionview"),
    path('checkout', views.checkout, name="checkout"),
    path('update_items/', views.updateItem, name="update_items"),
    path('process_order/', views.processOrder, name="process_order"),
]
