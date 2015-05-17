from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from mobilepsu_api import views

urlpatterns = [
    url(r'^fields/$', views.FieldList.as_view()),
    url(r'^fields/(?P<pk>[0-9]+)/$', views.FieldDetail.as_view()),
    url(r'^questions/$', views.QuestionList.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)