from django.conf.urls import url
from ocp import views


urlpatterns = [
    url(r'^proceso/$', views.proceso_list),
    url(r'^proceso/(?P<pk>[0-9]+)/$', views.proceso_detail),
]
