from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from mobilepsu_api import views

urlpatterns = [
    url(r'^fields/$', views.field_list),
    url(r'^fields/(?P<pk>[0-9]+)/$', views.field_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)