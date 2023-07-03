"""
URL configuration for plantshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include
=======
from django.urls import path, include
>>>>>>> a1cfe3135fb2b4a09571e81750125c86d237723d
from django.conf.urls.static import static
from django.conf import settings


<<<<<<< HEAD
admin.site.site_header ="Easy Gardening"
admin.site.site_title="Ifraj Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    #adding path
    
    path('',include('plantapp.urls')),
    path('authen/', include(('authen.urls','authen'), namespace='authen')),

    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
admin.site.site_header = "Easy Gardening"
admin.site.site_title = "Ifraj Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    # adding path

    path('', include('plantapp.urls')),
    path('authen/', include(('authen.urls', 'authen'), namespace='authen')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> a1cfe3135fb2b4a09571e81750125c86d237723d
