"""
URL configuration for flipkart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from electronics import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('electronics/', include('electronics.urls')),  # Replace 'your_app' with your actual app name
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.contrib import admin
from django.urls import path, include
from electronics import views


urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.home, name='home.html'),
    path('electronics/', include('electronics.urls')),
]
>>>>>>> aee1c01f7da304bc88bb1521251d8b687b9a59a6
