"""maziotis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from dhmoi.views import home
from django.views.generic import TemplateView
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('dhmoi.urls'), name='home'),
    url(r'^dhmoi/', include('dhmoi.urls')),
    url(r'^dhmos_new/', include('dhmoi.urls')),
    url(r'^employee/', include('dhmoi.urls')),
    url(r'^employee_new/', include('dhmoi.urls')),
    url(r'^aithmata/', include('dhmoi.urls')),
    url(r'^aithmata_new/', include('dhmoi.urls')),
    url(r'^service', include('dhmoi.urls')),
    url(r'^service_new/', include('dhmoi.urls')),
    url(r'^ergasies/', include('dhmoi.urls')),
    url(r'^ergasia_new/', include('dhmoi.urls')),
    url(r'^adeia/', include('dhmoi.urls')),
    url(r'^', include('dhmoi.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    
    ]

