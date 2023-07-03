from django.urls import path
from authen import views

urlpatterns = [
    #jump to views
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout')
]