#coding=utf8
from django.conf.urls import patterns, include, url

'''
Development
Support
UIVI
'''
urlpatterns = patterns('service.views',
    url(r'^Development/$','Development',name='Development'),
    url(r'^Support/$','Support',name='Support'),
    url(r'^UIVI/$','UIVI',name='UIVI'),
)