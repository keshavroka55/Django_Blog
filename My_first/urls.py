"""
URL configuration for My_first project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.load, name='load'),
    path('profile/', views.login_sucess, name = 'login_sucess'),
    path('homepage/', views.keshav_list, name = 'homepage'),

    # IMPORTANT ONE
    # while creating a sub file of app (keshav...)
    path('keshav/', include('keshav.urls')),

    # this is for in setting.py i added some URLS path of accounts, login, logout.
    path('accounts/', include('django.contrib.auth.urls')),


# this is the one which is need to determine the path of reload....
    path("__reload__/", include ("django_browser_reload.urls")),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
