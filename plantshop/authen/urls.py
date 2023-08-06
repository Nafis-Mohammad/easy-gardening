from django.urls import path
from authen import views
from django.conf.urls.static import static
from .views import profile
from django.conf import settings


urlpatterns = [
    # jump to views
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('profile/', views.profile, name='profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
