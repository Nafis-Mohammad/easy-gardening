from django.urls import path
from plantapp import views


urlpatterns = [
    # jump to views
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('carts', views.carts, name="carts"),
    path('store', views.store, name="store"),
    path('collection', views.collection, name="collection"),
    path('maintenance/<str:id>', views.collectionviewmaint,
         name="collectionviewmaint"),
    path('collection/<str:id>', views.collectionview, name="collectionview"),
    path('checkout', views.checkout, name="checkout"),
    path('update_items/', views.updateItem, name="update_items"),
    path('process_order/', views.processOrder, name="process_order"),
    path('thankyou/', views.thankyou_view, name='thankyou'),
    path('products/', views.product_list, name='product_list'),
    path('submit_review/<int:product_id>/',
         views.submit_review, name='submit_review'),

    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search_products', views.product_search, name='search_products'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('update_wish/', views.add_to_wishlist, name="update_wish"),

]
