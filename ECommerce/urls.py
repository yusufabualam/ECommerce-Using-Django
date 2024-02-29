"""
URL configuration for ECommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from product.views import *
from .views import *
from .settings import *

def basic(request):
    return render(request, 'basic.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProductListView.as_view()),
    path('accounts/register/', Registration.as_view(), name='register'),
    path('product/API/',include('product.api.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
