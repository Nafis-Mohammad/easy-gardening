from django.urls import path
from plantapp import views

urlpatterns = [
    #jump to views 
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),    
    path('product',views.product,name='product'),    

  
]