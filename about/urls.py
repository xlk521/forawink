#coding=utf8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('about.views',
    url(r'^$','about',name='about'),
)