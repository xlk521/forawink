#coding=utf8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('case.views',
    url(r'^$','case',name='case'),
)