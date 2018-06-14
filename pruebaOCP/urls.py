"""pruebaOCP URL Configuration

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
#from rest_framework import routers
from rest_framework_mongoengine import routers as merouters
from ocp import views

merouter = merouters.DefaultRouter()
merouter.register(r'procesos', views.getListProceso,base_name='Proceso')
merouter.register(r'getproceso', views.getCodigoProceso,base_name='Proceso')
merouter.register(r'getTipoProceso', views.getTipoProceso,base_name='Proceso')
merouter.register(r'getEntidadProceso', views.getEntidadProceso,base_name='Proceso')


urlpatterns = [
    url(r'^admin/', admin.site.urls),    
    url(r'^api/', include(merouter.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
